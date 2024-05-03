#importing json(javascript object notation)
import json

class workoutPlan:
    def __init__(self, athlete_id, name, level, exercises):
        self.athlete_id, self.name, self.level, self.exercises= athlete_id, name, level, exercises

class Athlete:
    def __init__(self):
        self.workout_plans = {}

    # create the  workout plan
    def create_workout_plan(self):
        athlete_id = input("Enter athlete id : ")
        if athlete_id in self.workout_plans:
            raise ValueError("Athlete id is already present")
        name = input("Enter name : ")
        level = input("Enter level like beginner,intermediate,advance : ")
        exercises = input("Enter exercises : ")
        if athlete_id in self.workout_plans:
            raise ValueError("Workout plan for athlete ID already exists")
        else:
            self.workout_plans[athlete_id] = workoutPlan(athlete_id, name, level, exercises)
            print("Workout plan CREATED successfully")

    # reading the workout plan
    def read_workout_plan(self):
        athlete_id = input("Enter athlete id : ")
        if athlete_id not in self.workout_plans:
            raise ValueError("Athlete ID does not exist")
        plan = self.workout_plans[athlete_id]
        print(f"Athlete ID: {plan.athlete_id}, Name: {plan.name}, Level: {plan.level}, Exercises: {plan.exercises}")

    # updating the workout plan
    def update_workout_plan(self):
        athlete_id = input("Enter athlete id : ")
        if athlete_id not in self.workout_plans:
            raise ValueError("Athlete ID does not exist")
        plan = self.workout_plans[athlete_id]
        name = input(f"Enter new name for athlete {athlete_id} (if needed to update,else skip/leave blank) : ")
        level = input(f"Enter new level for athlete {athlete_id} (if needed to update,else skip/leave blank) : ")
        exercises = input(f"Enter new exercises for athlete {athlete_id} (if needed to update,else skip/leave blank) : ")
        if name:
            plan.name = name
        if level:
            plan.level = level
        if exercises:
            plan.exercises = exercises
        print(f"Workout plan of athlete id {athlete_id} UPDATED successfully")

    # deleting the workout plan
    def delete_workout_plan(self):
        athlete_id = input("Enter athlete id: ")
        if athlete_id not in self.workout_plans:
            raise ValueError("Athlete ID does not exist")
        del self.workout_plans[athlete_id]
        print(f"workout plan of athlete id {athlete_id} is deleted successfully")

    # generate the custom workout
    def generate_custom_workouts(self):
        athlete_id = input("Enter athlete ID: ")
        custom_workout = [plan for plan in self.workout_plans.values() if plan.athlete_id == athlete_id]
        if not custom_workout:
            print("No workout plan found for this athlete")
            return
        for plan in custom_workout:
            print(f"Athlete ID: {plan.athlete_id}, Name: {plan.name}, Level: {plan.level}, Exercises: {plan.exercises}")
    
    #saving the data to the file
    def save_data_to_file(self, filename):
        with open(filename, 'w') as json_file:
            json.dump([plan._dict_ for plan in self.workout_plans.values()], json_file)
    
    #load the data frm file 
    def load_data_from_file(self, filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            for plan_data in data:
                plan = workoutPlan(plan_data['athlete_id'], plan_data['name'], plan_data['level'], plan_data['exercises'])
                self.workout_plans[plan.athlete_id] = plan
    
    #menu driven
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Create plan")
            print("2. Read Plan")
            print("3. Update Plan")
            print("4. Delete plan")
            print("5. Generate Custom Workouts")
            print("6. Save data into File")
            print("7. Load data from File")
            print("8. Exit")

            choice = input("Enter your choice : ")

            if choice == '1':
                self.create_workout_plan()
            elif choice == '2':
                self.read_workout_plan()
            elif choice == '3':
                self.update_workout_plan()
            elif choice == '4':
                self.delete_workout_plan()
            elif choice == '5':
                self.generate_custom_workouts()
            elif choice == '6':
                self.save_data_to_file('workout_plans.json')
            elif choice == '7':
                self.load_data_from_file('workout_plans.json')
            elif choice == '8':
                print("Exiting program...")
                break
            else:
                print("Invalid choice, enter the choice 1 to 8")

athlete_manager = Athlete() #class object
athlete_manager.menu() #calling menu function