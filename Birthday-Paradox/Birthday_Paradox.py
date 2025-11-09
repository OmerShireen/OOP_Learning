import random

class BirthdayParadoxSimulator:
    def __init__(self, num_trials=10000):
        """
        Initialize the simulator with a number of trials for each group size.
        """
        self.num_trials = num_trials

    @staticmethod
    def has_duplicate_birthdays(n):
        """
        Returns True if at least two people in a group of n
        have the same birthday, otherwise False.
        """
        birthdays = [random.randint(1, 365) for _ in range(n)]
        return len(birthdays) != len(set(birthdays))

    def simulate_for_group(self, n):
        """
        Runs the simulation for a group of size n and returns the probability
        of at least two people sharing a birthday.
        """
        count = 0
        for _ in range(self.num_trials):
            if self.has_duplicate_birthdays(n):
                count += 1
        return count / self.num_trials

    def run_simulation(self, start=5, end=100, step=5):
        """
        Simulates the birthday paradox for group sizes from start to end
        and prints the estimated probabilities.
        """
        print("Group Size (n)\tProbability of Shared Birthday")
        for n in range(start, end + 1, step):
            probability = self.simulate_for_group(n)
            print(f"{n}\t\t{probability:.4f}")


# Example usage
simulator = BirthdayParadoxSimulator(num_trials=10000)
simulator.run_simulation()
