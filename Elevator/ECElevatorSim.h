//  ElevatorSimRequest Class Created by Professor Yufeng Wu on 6/27/23
//  All other code created by Donald Bailey
//  Elevator simulation

#ifndef ECElevatorSim_h
#define ECElevatorSim_h

#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <string> 
#include <cmath>

//*****************************************************************************
// DON'T CHANGE THIS CLASS
// 
// Elevator simulation request: 
// (i) time: when the request is made
// (ii) floorSrc: which floor the user is at at present
// (iii) floorDest floor: where the user wants to go; we assume floorDest != floorSrc
// 
// Note: a request is in three stages:
// (i) floor request: the passenger is waiting at floorSrc; once the elevator arrived 
// at the floor (and in the right direction), move to the next stage
// (ii) inside request: passenger now requests to go to a specific floor once inside the elevator
// (iii) Once the passenger arrives at the floor, this request is considered to be "serviced"

class ECElevatorSimRequest
{
public:
    ECElevatorSimRequest(int timeIn, int floorSrcIn, int floorDestIn) : time(timeIn), floorSrc(floorSrcIn), floorDest(floorDestIn), fFloorReqDone(false), fServiced(false), timeArrive(-1) {} 
    ECElevatorSimRequest(const ECElevatorSimRequest &rhs) : time(rhs.time), floorSrc(rhs.floorSrc), floorDest(rhs.floorDest), fFloorReqDone(rhs.fFloorReqDone), fServiced(rhs.fServiced), timeArrive(rhs.timeArrive) {}
    int GetTime() const {return time; }
    int GetFloorSrc() const { return floorSrc; }
    int GetFloorDest() const { return floorDest; }
    bool IsGoingUp() const { return floorDest >= floorSrc; }

    // Is this passenger in the elevator or not
    bool IsFloorRequestDone() const { return fFloorReqDone; }
    void SetFloorRequestDone(bool f) { fFloorReqDone = f; }

    // Is this event serviced (i.e., the passenger has arrived at the desstination)?
    bool IsServiced() const { return fServiced; }
    void SetServiced(bool f) { fServiced = f; }

    // Get the floor to service
    // If this is in stage (i): waiting at a floor, return that floor waiting at
    // If this is in stage (ii): inside an elevator, return the floor going to
    // Otherwise, return -1
    int GetRequestedFloor() const {
        if( IsServiced() )  {
            return -1;
        }
        else if( IsFloorRequestDone() )   {
            return GetFloorDest();
        }
        else {
            return GetFloorSrc();
        }
    }

    // Wait time: get/set. Note: you need to maintain the wait time yourself!
    int GetArriveTime() const { return timeArrive; }
    void SetArriveTime(int t) { timeArrive = t; }

private:
    int time;           // time of request made
    int floorSrc;       // which floor the request is made
    int floorDest;      // which floor is going
    bool fFloorReqDone; // is this passenger passing stage one (no longer waiting at the floor) or not
    bool fServiced;     // is this request serviced already?
    int timeArrive;     // when the user gets to the desitnation floor
};

//*****************************************************************************
// Elevator moving direction

typedef enum
{
    EC_ELEVATOR_STOPPED = 0,    // not moving
    EC_ELEVATOR_UP = 1,             // moving up
    EC_ELEVATOR_DOWN = 2            // moving down
} EC_ELEVATOR_DIR;

//*****************************************************************************
// Code below created by Donald Bailey

//parent state class 
class ElevState
{
public:
    ~ElevState() {} //destructor
    virtual void GetNextState() = 0;
    virtual EC_ELEVATOR_DIR GetNextDir() const = 0;
    virtual int GetState() const = 0;
    
};

//moving state
class ElevStateMoving : public ElevState
{
public:

    //constructor
    ElevStateMoving(EC_ELEVATOR_DIR cur_dir, int cur_floor, int cur_state, int t, std::vector<ECElevatorSimRequest> &list_requests, std::vector<int> &onboard_requests, std::vector<int> &floor_requests) : cur_dir(cur_dir), floor_requests(floor_requests), onboard_requests(onboard_requests), list_requests(list_requests), cur_floor(cur_floor), state(cur_state), time(t) {}
    virtual void GetNextState() override;
    virtual EC_ELEVATOR_DIR GetNextDir() const override {return next_dir;}
    virtual int GetState() const override {return state;}

private:
    std::vector<ECElevatorSimRequest> &list_requests; //all requests
    std::vector<int> &onboard_requests; //people in the elevator
    std::vector<int> &floor_requests; //people on a floor
    EC_ELEVATOR_DIR cur_dir; //current direction
    EC_ELEVATOR_DIR next_dir; //next direction
    int state; //state to be updated
    int cur_floor;
    int time;
};

//stopped state
class ElevStateStopped : public ElevState
{
public:

    //constructor
    ElevStateStopped(EC_ELEVATOR_DIR cur_dir, int cur_floor, int cur_state, int t, std::vector<ECElevatorSimRequest> &list_requests, std::vector<int> &onboard_requests, std::vector<int> &floor_requests) : cur_dir(cur_dir), onboard_requests(onboard_requests), floor_requests(floor_requests), list_requests(list_requests), cur_floor(cur_floor), state(cur_state), time(t) {}
    virtual void GetNextState() override;
    virtual EC_ELEVATOR_DIR GetNextDir() const override {return next_dir;}
    virtual int GetState() const override {return state;}

private:
    std::vector<ECElevatorSimRequest> &list_requests; //all requests
    std::vector<int> &onboard_requests; //people in the elevator
    std::vector<int> &floor_requests; //people on a floor
    EC_ELEVATOR_DIR cur_dir; //current direction
    EC_ELEVATOR_DIR next_dir; //next direction
    int state; //state to be updated
    int cur_floor;
    int time; 
};

class ElevStateBoarding : public ElevState
{
public:
    //constructor
    ElevStateBoarding(EC_ELEVATOR_DIR cur_dir, int cur_floor, int prev_floor, int cur_state, int t, std::vector<ECElevatorSimRequest> &list_requests, std::vector<int> &onboard_requests, std::vector<int> &floor_requests) : cur_dir(cur_dir), prev_floor(prev_floor), onboard_requests(onboard_requests), floor_requests(floor_requests), list_requests(list_requests), cur_floor(cur_floor), state(cur_state), time(t) {}
    virtual void GetNextState() override;
    virtual EC_ELEVATOR_DIR GetNextDir() const override {return next_dir;}
    virtual int GetState() const override {return state;}

private:
    std::vector<ECElevatorSimRequest> &list_requests; //all requests
    std::vector<int> &onboard_requests; //people in elevator
    std::vector<int> &floor_requests; //people on a floor
    EC_ELEVATOR_DIR cur_dir; //curent direction
    EC_ELEVATOR_DIR next_dir; //next direction
    int state; // state that will be updated
    int prev_floor;
    int cur_floor;
    int time;
};

//*****************************************************************************
// Simulation of elevator

class ECElevatorSim
{
public:
    // numFloors: number of floors serviced (floors numbers from 1 to numFloors)
    ECElevatorSim(int numFloors, std::vector<ECElevatorSimRequest> &listRequests) : num_floors(numFloors), list_requests(listRequests) {}

    // free buffer
    ~ECElevatorSim() {}

    // Simulate by going through all requests up to certain period of time (as specified in lenSim)
    // starting from time 0. For example, if lenSim = 10, simulation stops at time 10 (i.e., time 0 to 9)
    // Caution: the list of requests contain all requests made at different time;
    // at a specific time of simulation, some events may be made in the future (which you shouldn't consider these future requests)
    void Simulate(int lenSim);

    // The following methods are about querying/setting states of the elevator
    // which include (i) number of floors of the elevator, 
    // (ii) the current floor: which is the elevator at right now (at the time of this querying). Note: we don't model the tranisent states like when the elevator is between two floors
    // (iii) the direction of the elevator: up/down/not moving

    // Get num of floors
    int GetNumFloors() const {return num_floors;}

    // Get current floor
    int GetCurrFloor() const {return cur_floor;};

    // Set current floor
    void SetCurrFloor(int f) {cur_floor = f;};

    // Get current direction
    EC_ELEVATOR_DIR GetCurrDir() const {return cur_dir;};

    // Set current direction
    void SetCurrDir(EC_ELEVATOR_DIR dir) {cur_dir = dir;};

    //copy the history of movement for the front end
    void GetDirHist(std::vector<EC_ELEVATOR_DIR> &hist)
    {
        for(auto dir: dir_hist)
        {
            hist.push_back(dir);
        }
    };

private:

    int num_floors; // number of floors
    int cur_floor; //current floor
    int prev_floor; //prev floor for tracking
    std::vector<ECElevatorSimRequest> &list_requests; //request list
    std::vector<int> onboard_requests; //all requests for people on the elevator
    std::vector<int> floor_requests; //all requests for people on a floor
    EC_ELEVATOR_DIR cur_dir; //current direction
    std::vector<EC_ELEVATOR_DIR> dir_hist; //history of directions
};


#endif /* ECElevatorSim_h */
