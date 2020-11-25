# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
    def insert(self, node, handler):
        # Insert the node as before
        self.children[node] = RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr = self.root
        for word in path:
            if word not in curr.children:
                curr.children[word] = RouteTrieNode(None)
            curr = curr.children[word]
        curr.handler = handler
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(path) == 0:
            return self.root.handler
        curr = self.root
        for word in path:
            if word in curr.children:
                curr = curr.children[word]
            else:
                return None
        return curr.handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler)
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        return self.root.insert(path_list, handler)
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.root.find(path_list)
    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == "/":
            return []
        split_path = path.split('/')
        while '' in split_path:
            split_path.remove('')
        return split_path

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route

# Test 0
print("test 0...")
router = Router("root handler")
router.add_handler("", "")  # add a route
print(router.lookup("")) # should print blank line
print(router.lookup("/")) # should print blank line
router.add_handler("/home/about", "about handler")  # add a route
print(router.lookup("")) # should print blank line
print(router.lookup("/")) # should print blank line
# Test 1
print("test 1...")
#router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print None
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler', handled trailing slashes
print(router.lookup("/home/about/me")) # should print None
router.add_handler("/home/about/me/", "me handler")  # add a route
print(router.lookup("/home/about/me")) # should print 'me handler'
print(router.lookup("/home/abut/me")) # should print None
# Test 2
print("test 2...")
router = Router("root handler")
router.add_handler("/", "home handler")  # add a route
print(router.lookup("/")) # should print 'home handler'
print(router.lookup("/home")) # should print None
