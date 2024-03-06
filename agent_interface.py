class DiceAdventureAgent:
    """
    Provides a uniform interface to connect agents to Dice Adventure environment.
    Developers must implement the load() and take_action() functions.
    - init()        - optional: initialize any needed variables
    - load_agent()  - required: Loads and returns your agent
    - take_action() - required: Determines which action to take given a state (dict) and list of actions. Note that your
                                agent does not need to use the list of actions, it is just provided for convenience.
    """
    def __init__(self):
        self.agent = None

    def load_agent(self):
        """
        Loads and sets the 'self.agent' variable. If you prefer to do this in the init() function, this function
        can be left unimplemented.
        :return:
        """
        pass

    def take_action(self, state, actions):
        """
        Given a game state and list of actions, the agent should determine which action to take and return a
        string representation of the action.
        :param state: (dict) A 'Dice Adventure' game state
        :param actions: (list) A list of string action names
        :return: (string) An action from the 'actions' list
        """
        pass