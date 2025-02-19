//  Code by Donald Bailey
//  Elevator simulation


#include "ECElevatorSim.h"

using namespace std;
//
//ECElevatorSim interface functions
//

//update floor
void ChangeFloor(EC_ELEVATOR_DIR dir, int &cur_floor, int &prev_floor)
{
    if(dir == EC_ELEVATOR_DOWN)
    {
        prev_floor = cur_floor;
        cur_floor--;
    } 
    if(dir == EC_ELEVATOR_UP)
    {
        prev_floor = cur_floor;
        cur_floor++;
    }
}

//update all onboard requests
void UpdateOnboard(std::vector<int> &onboard, std::vector<ECElevatorSimRequest> const list)
{
    onboard.clear();
    int index = 0;
    for(auto x: list)
    {
        if(x.IsFloorRequestDone() && !x.IsServiced())
        {
            onboard.push_back(index);
        }
        index++;
    }
}

//update all floor requests
void UpdateFloorRequests(int time, std::vector<int> &floor_requests, std::vector<ECElevatorSimRequest> const list)
{
    floor_requests.clear();
    int index = 0;
    for(auto x: list)
    {
        if(x.GetTime() <= time && !x.IsFloorRequestDone())
        {
            floor_requests.push_back(index);
        }
        index++;
    }
}

//update the direction the elevator is supposed to be headed in
EC_ELEVATOR_DIR Update(int cur_floor, EC_ELEVATOR_DIR prev_dir, std::vector<int> &floor_requests, std::vector<int> &onboard, std::vector<ECElevatorSimRequest> const list)
{
    for(auto x: floor_requests)
    {
        if((list[x].GetFloorSrc() < cur_floor) && (prev_dir == EC_ELEVATOR_DOWN))
        {
            return EC_ELEVATOR_DOWN;
        }

        if((list[x].GetFloorSrc() > cur_floor) && (prev_dir == EC_ELEVATOR_UP))
        {
            
            return EC_ELEVATOR_UP;
        }
    }
    for(auto i: onboard)
    {
        if((list[i].GetFloorDest() < cur_floor) && (prev_dir == EC_ELEVATOR_DOWN))
        {
            return EC_ELEVATOR_DOWN;
        }

        if((list[i].GetFloorDest() > cur_floor) && (prev_dir == EC_ELEVATOR_UP))
        {
            
            return EC_ELEVATOR_UP;
        }
    }
    if(prev_dir == EC_ELEVATOR_DOWN)
    {
        return EC_ELEVATOR_UP;
    }
    else
    {
        return EC_ELEVATOR_DOWN;
    }
}

//simulate
void ECElevatorSim :: Simulate(int lenSim)
{
    //init the base state
    SetCurrDir(EC_ELEVATOR_STOPPED);
    SetCurrFloor(1);
    ElevState *cur_state = new ElevStateStopped(cur_dir, cur_floor, 1, 0, list_requests, onboard_requests, floor_requests);
    
    //loop over time
    for(int i = 0; i <= lenSim; i++)
    {
        //update vectors and get new info to be passed into next state
        UpdateOnboard(onboard_requests, list_requests);
        UpdateFloorRequests(i, floor_requests, list_requests);
        cur_state->GetNextState();
        cur_dir = cur_state->GetNextDir();
        dir_hist.push_back(cur_dir);
        
        //update floor if not at edge
        if(cur_floor != 0 || cur_floor != num_floors)
        {
            ChangeFloor(cur_dir, cur_floor, prev_floor);
        }
        int state = cur_state->GetState();

        if(state == 0)
        {
            cur_state = new ElevStateMoving(cur_dir, cur_floor, state, i+1, list_requests, onboard_requests, floor_requests);
        }

        if(state == 1)
        {
            cur_state = new ElevStateStopped(cur_dir, cur_floor, state, i+1, list_requests, onboard_requests, floor_requests);
        }

        if(state == 2)      
        {
            cur_state = new ElevStateBoarding(cur_dir, cur_floor, prev_floor, state, i+1, list_requests, onboard_requests, floor_requests);
        }     
    }
}

//
//ECElevState interface functions
//

//find next state based on moving
void ElevStateMoving :: GetNextState()
{
    //if someone needs to get on
    if(floor_requests.size() != 0)
    {
        for(auto x: floor_requests)
        {
            if(list_requests[x].GetRequestedFloor() == cur_floor)
            {
                next_dir = EC_ELEVATOR_STOPPED;
                state = 2;
                break;
            }
        }
    }

    //if someone needs to get off
    if(onboard_requests.size() != 0)
    {
        for(auto i: onboard_requests)
        {
            if(list_requests[i].GetRequestedFloor() == cur_floor)
            {
                next_dir = EC_ELEVATOR_STOPPED;
                state = 2;
                break;
            }
        }
    }

    //if it wasn't found that someone needs to get on or off keep moving
    if(state != 2)
    {
        next_dir = cur_dir;
        state = 0;
    }
}

//find next state based on being stopped
void ElevStateStopped :: GetNextState()
{
    //loop over people until you find the first request
    int decided_floor = 0;
    for(auto x: list_requests)
    {
        if(x.GetTime() == time)
        {
            int get = x.GetFloorSrc();
            if(get == cur_floor)
            {
                state = 0;
                decided_floor = x.GetFloorDest();
                if(cur_floor < decided_floor)
                {
                    next_dir = EC_ELEVATOR_UP;
                }
                else
                {
                    next_dir = EC_ELEVATOR_DOWN;
                }  
            }
            else 
            {
                state = 0;
                decided_floor = x.GetFloorSrc();
                if(decided_floor < cur_floor)
                {
                    next_dir = EC_ELEVATOR_DOWN;
                }
                else
                {   
                    next_dir = EC_ELEVATOR_UP;
                }
            }
            break;
        }
    }

    //if stopped on a floor someone wants to get on
    for(auto i: floor_requests)
     {
        if(list_requests[i].GetRequestedFloor() == cur_floor)
        {
            list_requests[i].SetFloorRequestDone(true);
        }
    }
    UpdateOnboard(onboard_requests, list_requests);
    UpdateFloorRequests(time, floor_requests, list_requests);
}

//find next state based on having to board
void ElevStateBoarding :: GetNextState()
{
    //let people off
    for(auto x: onboard_requests)
    {
        if(list_requests[x].GetRequestedFloor() == cur_floor)
        {
            list_requests[x].SetArriveTime(time - 1);
            list_requests[x].SetServiced(true);
        }
    }
    //let people on
    for(auto i: floor_requests)
     {
        if(list_requests[i].GetRequestedFloor() == cur_floor && list_requests[i].GetTime() != time)
        {
            list_requests[i].SetFloorRequestDone(true);
        }
    }
    UpdateOnboard(onboard_requests, list_requests);
    UpdateFloorRequests(time, floor_requests, list_requests);

    //stop if no requests
    if(onboard_requests.empty() && floor_requests.empty())
    {
        state = 1;
        next_dir = EC_ELEVATOR_STOPPED;
    } 

    //update new direction
    else
    {
        EC_ELEVATOR_DIR prev_dir;
        if(cur_floor > prev_floor)
        {
            prev_dir = EC_ELEVATOR_UP;
        }
        else
        {
            prev_dir = EC_ELEVATOR_DOWN;
        }

        state = 0;
        next_dir = Update(cur_floor, prev_dir, floor_requests, onboard_requests, list_requests);

    }
}



