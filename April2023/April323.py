# For this kata you will be using some meta-programming magic to create a new Thing object. This object will allow you to define things in a descriptive sentence like format.
# This challenge attempts to build on itself in an increasingly complex manner.
# Examples of what can be done with "Thing":
# jane = Thing('Jane')
# jane.name # => 'Jane'
# # can define boolean methods on an instance
# jane.is_a.person
# jane.is_a.woman
# jane.is_not_a.man
# jane.is_a_person # => True
# jane.is_a_man # => False
# # can define properties on a per instance level
# jane.is_the.parent_of.joe
# jane.parent_of # => 'joe'
# # can define number of child things
# # when more than 1, a tuple subclass is created
# jane.has(2).legs
# len(jane.legs) # => 2
# isinstance(jane.legs[0], Thing) # => True
# # can define single items
# jane.has(1).head
# isinstance(jane.head, Thing) # => True
# # can define number of things in a chainable and natural format
# >> Note: Python, unlike Ruby and Javascript, doesn't have a pretty syntax for blocks of expressions and a forEach method for iterables. So you should implement this behaviour yourself.
# jane.has(2).arms.each.having(1).hand.having(5).fingers
# len(jane.arms[0].hand.fingers) # => 5
# # can define properties on nested items
# jane.has(1).head.having(2).eyes.each.being_the.color.blue.having(1).pupil.being_the.color.black
# # can define methods: thing.can.verb(method, past='')
# method = lambda phrase: "%s says: %s" % (name, phrase)
# # or 
# def method(phrase):
#   return "%s says: %s" % (name, phrase)
# jane.can.speak(method, "spoke")
# jane.speak("hello") # => "Jane says: hello"
# # if past tense was provided then method calls are tracked
# jane.spoke # => ["Jane says: hello"]

class Thing:
    def __init__(self, name):
        self.name = name
        self.properties = {}
        self.children = {}
        self.methods = {}

    def __getattr__(self, attr):
        if attr.startswith('is_a_'):
            class_name = attr[5:]
            self.properties[class_name] = True
            return True
        elif attr.startswith('is_not_a_'):
            class_name = attr[9:]
            self.properties[class_name] = False
            return True
        elif attr.startswith('is_the_'):
            property_name = attr[8:]
            self.properties[property_name] = None
            return self
        elif attr.startswith('has_'):
            class_name = attr[4:]
            self.children[class_name] = []
            return self
        elif attr == 'having':
            return self
        elif attr == 'each':
            return self.children.values()
        elif attr == 'can':
            return self
        else:
            return self.methods[attr]

    def __setattr__(self, attr, value):
        if attr.startswith('is_the_'):
            property_name = attr[8:]
            self.properties[property_name] = value
        else:
            super().__setattr__(attr, value)

    def __call__(self, *args, **kwargs):
        if 'having' in kwargs:
            child_name = kwargs['having']
            child = Thing(child_name)
            self.children[self.current_child_type()].append(child)
            return child
        elif 'method' in kwargs:
            method_name = args[0]
            past_tense = kwargs.get('past', None)
            self.methods[method_name] = {
                'method': args[1],
                'past_tense': past_tense,
                'calls': []
            }
        elif len(args) > 0:
            property_name = args[0]
            self.properties[property_name] = args[1]
        else:
            return self

    def current_child_type(self):
        for k, v in self.children.items():
            if len(v) < self.child_quantity:
                return k

    def has(self, quantity):
        self.child_quantity = quantity
        return self

    def __getitem__(self, item):
        return self.children[item][0] if len(self.children[item]) == 1 else tuple(self.children[item])

    def __repr__(self):
        return f"<Thing '{self.name}'>"

    def __str__(self):
        return self.name
