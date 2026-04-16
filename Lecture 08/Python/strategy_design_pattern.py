from abc import ABC, abstractmethod

class WalkAbleRobot(ABC):
    @abstractmethod
    def walk(self):
        pass

class NormalWalk(WalkAbleRobot):
    def walk(self):
        print("Walking Normally")
    
class NoWalk(WalkAbleRobot):
    def walk(self):
        print("Cannot walk")


class TalkAbleRobot(ABC):
    @abstractmethod
    def talk(self):
        pass

class NormalTalk(TalkAbleRobot):
    def talk(self):
        print("Talking Normally")
    
class NoTalk(TalkAbleRobot):
    def talk(self):
        print("Cannot talk")
    
class FlyAbleRobot(ABC):
    @abstractmethod
    def fly(self):
        pass

class NormalFly(FlyAbleRobot):
    def fly(self):
        print("Flying Normally")
    
class NoFly(FlyAbleRobot):
    def fly(self):
        print("Cannot fly")


class Robot(ABC):
    def __init__(self, walk_able_robot: WalkAbleRobot, talk_able_robot: TalkAbleRobot, fly_able_robot: FlyAbleRobot):
        self._walk_behavior = walk_able_robot
        self._talk_behavior = talk_able_robot
        self._fly_behavior = fly_able_robot
    
    def walk(self):
        self._walk_behavior.walk()
    
    def talk(self):
        self._talk_behavior.talk()

    def fly(self):
        self._fly_behavior.fly()
    
    @abstractmethod
    def projection(self):
        pass

class CompanionRobot(Robot):
    def __init__(self, walk_able_robot, talk_able_robot, fly_able_robot):
        super().__init__(walk_able_robot, talk_able_robot, fly_able_robot)
    
    def projection(self):
        print("Displaying Projection for companion Robot")

class WorkerRobot(Robot):
    def __init__(self, walk_able_robot, talk_able_robot, fly_able_robot):
        super().__init__(walk_able_robot, talk_able_robot, fly_able_robot)
    
    def projection(self):
        print("Displaying Projection for Worker Robot")

    
if __name__ == "__main__":
    robot1 = CompanionRobot(NormalWalk(), NormalTalk(), NormalFly())
    robot1.walk()
    robot1.talk()
    robot1.fly()
    robot1.projection()


    print("-------------------")

    robot2 = WorkerRobot(NoWalk(), NoTalk(), NormalFly())
    robot2.walk()
    robot2.talk()
    robot2.fly()
    robot2.projection()

    