import unittest #unitttest module is imported for performing unittest
class workoutplan:
    def __init__(self,athelete_id, name, level, exercises):
        self.athelete_id, self.name, self.level, self.exercises = athelete_id, name, level, exercises

#CRUD operation

class Athelete:
    def __init__(self):
        self.workout_plans = {}

    #create the  workout plan
    def create_athelete_workout_plan(self, athelete_id, name, level, exercises):
        if athelete_id in self.workout_plans:
            raise ValueError("workout athlete ID already exists") #raise the value error if athelete id is does not exist
        else:
            self.workout_plans[athelete_id] = workoutplan(athelete_id, name, level, exercises)

    #reading the workout plan
    def read_athelete_workout_plan(self, athelete_id):
        if athelete_id not in self.workout_plans:
            raise ValueError("Athlete ID does not exist") #raise the value error if athelete id is does not exist
        else:
            return self.workout_plans.get(athelete_id)

    #updating the workout plan
    def update_athelete_workout_plan(self, athelete_id, name = None, level = None, exercises = None):
        workout_plan = self.workout_plans.get(athelete_id)
        if workout_plan is None:
            raise ValueError("Athlete ID does not exist") #raise the value error if athelete id is does not exist
        if name:
            workout_plan.name = name
        if level:
            workout_plan.level = level
        if exercises:
            workout_plan.exercises = exercises

    #deleting the workout plan
    def delete_athelete_workout_plan(self, athelete_id):
        if athelete_id not in self.workout_plans:
            raise ValueError("Athelete ID does not exist") #raise the value error if athelete id is does not exist
        else:
            del self.workout_plans[athelete_id]

    #generate the custom workout
    def generate_custom_workouts(self, athelete_id):
        custom_workout = []
        for workoutplan in self.workout_plans.values():
            if workoutplan.athelete_id == athelete_id:
                custom_workout.append(workoutplan)
        return custom_workout

    #monitor the workout completion
    def monitor_workout_completion(self, completion_data):
        plan_id = completion_data.get('plan_id')
        if plan_id not in self.workout_plans:
            raise ValueError("Athlete plan ID does not exist") #raise the value error if athelete id is does not exist
        else:
            print("Workout completed for plan ID {}: {}".format(plan_id, completion_data))

#Unit test
class Testworkoutplanner(unittest.TestCase):

    def setUp(self):
        self.plan = Athelete()
        self.plan.create_athelete_workout_plan(1,'abc', 'beginner', 'push-ups') #first athelete details : athelete id, name, level, exercise
        self.plan.create_athelete_workout_plan(2,'def','intermediate','Running') #second athelete details : athelete id, name, level, exercise
        self.workout_plan = self.plan

    def test_create_workout_plan(self):
        self.plan.create_athelete_workout_plan(3,'xyz','advanced','pull-ups')#create new athelete workout plan
        self.assertIn(3, self.plan.workout_plans)#insert into the list

    def test_get_workout_plan(self):
        plan = self.plan.read_athelete_workout_plan(1)
        self.assertEqual(plan.athelete_id,1)

    def test_update_workout_plan(self):
        self.plan.update_athelete_workout_plan(1, name = 'fgh', level = 'intermediate', exercises = 'Squats')
        plan = self.plan.read_athelete_workout_plan(1)#update name, level, exerxises to the athelete id 1
        self.assertEqual(plan.name,'fgh') #update name
        self.assertEqual(plan.level,'intermediate')#update level
        self.assertEqual(plan.exercises, 'Squats') #update exercises

    def test_delete_workout_plan(self):
        self.plan.delete_athelete_workout_plan(2) #delete the workout plan of athelete id 2
        self.assertNotIn(2,self.plan.workout_plans)

    def test_generate_custom_workouts(self):
        custom_workouts = self.plan.generate_custom_workouts(1)
        self.assertEqual(custom_workouts[0].athelete_id,1)

    def test_monitor_workout_completion_invalid_plan(self):
        completion_data = {'plan_id': 3, 'completion_time': '2024-04-29 08:00:00', 'duration_minutes': 45}
        with self.assertRaises(ValueError) as context:
           self.workout_plan.monitor_workout_completion(completion_data)
        self.assertEqual(str(context.exception), "Athlete plan ID does not exist")

if __name__ == '__main__':
    unittest.main(verbosity=2)