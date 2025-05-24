__author__ = "Anthony Zhuang"
__copyright__ = "Copyright 2009-2025"
__license__ = "MIT License"

import URBasic
#import URplus #import if any UPplus modules is needed

class RobotConnector(object):
    '''
    Class to hold all connection to the Universal Robot and plus devises  
         
    Input parameters:

    '''


    def __init__(self,robotModel, host, hasForceTorque=False):
        '''
        Constructor see class description for more info.
        '''
        if(False):
            assert isinstance(robotModel, URBasic.robotModel.RobotModel)  ### This line is to get code completion for RobotModel
        self.RobotModel = robotModel
        self.RobotModel.ipAddress = host
        self.RobotModel.hasForceTorqueSensor = hasForceTorque
        self.RealTimeClient = URBasic.realTimeClient.RealTimeClient(robotModel)
        self.RTDE = URBasic.rtde.RTDE(robotModel)
        self.DashboardClient = URBasic.dashboard.DashBoard(robotModel)
        self.ForceTourqe = None
        if hasForceTorque:
            self.ForceTourqe = URplus.forceTorqueSensor.ForceTorqueSensor(robotModel)
        


    def close(self):
        self.RTDE.close()
        self.RealTimeClient.Disconnect()
        self.DashboardClient.close()
        if self.ForceTourqe is not None:
            self.ForceTourqe.close()
