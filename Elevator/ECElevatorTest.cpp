// Testing elevators

#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include "ECElevatorSim.h"
#include "ECElevatorSim.cpp"

using namespace std;

// Test utility 
template<class T>
void ASSERT_EQ(T x, T y)
{
  if( x == y )
  {
    cout << "Test passed: equal: " << x << "  " << y << endl;
  }
  else
  {
    cout << "Test FAILED: equal: " << x << "  " << y << endl;
  }
}

static void RunTest(int numFloors, int timeSim, vector<ECElevatorSimRequest> &listRequests, vector<int> &listArriveTime )
{
    // simulate
    ECElevatorSim sim(numFloors, listRequests );
    sim.Simulate(timeSim);

    // status of requests
    for(unsigned int i=0; i<listRequests.size(); ++i)
    {
        //cout << "Request " << i << ": ";
        int tmDone = listRequests[i].GetArriveTime();
        ASSERT_EQ(tmDone, listArriveTime[i] );
#if 0
        if( tmDone >= 0 )
        {
            cout << "arrived at time " << tmDone;
        }
        else
        {
            cout << " hasn't arrived yet";
        }
        cout << endl;
#endif
    }
}

// a simple test: a single passenger going from floor 3 to 1
// this passenger arrived time 7: 
// (i) elevator gets to floor 3 at time 4 (received request from this passenger at time 2);
// (ii) wait for time 1 to let the passenger in the elevator (now time 5)
// (iii) move to floor 1 from 3, which takes time 6 and 7; so arrive at floor 1 (destination) at time 7

static void Test0()
{
    cout << "\n****** TEST 0\n";
    // test setup
    const int NUM_FLOORS = 7;
    const int timeSim = 10;
    ECElevatorSimRequest r1(2, 3, 1);
    vector<ECElevatorSimRequest> listRequests;
    listRequests.push_back(r1);
    vector<int> listArriveTime;
    listArriveTime.push_back(7);

    // request for elevator at time 2, arrive at time 7
    RunTest(NUM_FLOORS, timeSim, listRequests, listArriveTime);
}

// Two passengers: 
// Passenger 1: arrived time 7: 
// (i) elevator gets to floor 3 at time 4 (received request from this passenger at time 2);
// (ii) wait for time 1 to let the passenger in the elevator (now time 5)
// (iii) move to floor 3 from 5, which takes time 6 and 7; so arrive at floor 5 (destination) at time 7
// Passenger 2: 
// (i) elevator arrives at floor 6 at time 9 (note: unloading at time 8 at floor 5)
// (ii) move downwards starting at time 10; take 6 time units to get to floor 1 (arrived at floor 1 at time 15)
static void Test1()
{
    cout << "\n****** TEST 1\n";
    // test setup
    const int NUM_FLOORS = 7;
    const int timeSim = 20;
    ECElevatorSimRequest r1(2, 3, 5), r2(2, 6, 1);
    vector<ECElevatorSimRequest> listRequests;
    listRequests.push_back(r1);
    listRequests.push_back(r2);
    vector<int> listArriveTime;
    listArriveTime.push_back(7);
    listArriveTime.push_back(15);

    // simulate
    RunTest(NUM_FLOORS, timeSim, listRequests, listArriveTime);
}

int main(int argc, char** argv)
{
    //Test with files
    //Uncomment the below code if you wish to enter in your test files
    /*
    std::ifstream infile(argv[1]);
    std::string line;
    std::vector<int> v;
    while (std::getline(infile, line))
    {
        std::istringstream iss(line);
        int n;
        while (iss >> n)
        {
            v.push_back(n);
        }

    }
    for(auto i: v)
    {
        cout << i << endl;
    }

    int requests = v.size()/3;
    int count  = 2;

    const int NUM_FLOORS = v[0];
    const int timeSim = v[1];
    vector<ECElevatorSimRequest> listRequests;
    for(int i = 0; i < requests; i++)
    {
        listRequests.push_back(ECElevatorSimRequest(v[count], v[count + 1], v[count + 2]));
        count += 3;
    }

    ECElevatorSim sim(NUM_FLOORS, listRequests);

    vector<EC_ELEVATOR_DIR> dir;
    */
    
   
    //Create more tests if necessary
    Test0();
    Test1();

}
