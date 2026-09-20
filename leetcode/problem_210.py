### Problem 21. Course Schedule-II
### tags: graphs, topological sort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        # 2 -> 3 ->0 -> 1

        # pre-requiste to course
        # adj = {
        # 0: [],
        # 1: [0],
        # 2: [0, 3]
        # 3: []
        # }

                        #    0 <- 1, 0 <- 2, 3 <-2
        # prerequisites = [[0, 1], [0, 2], [3, 2]]     
        # course = 4   
        # courses_completed = 1
        # node defines a course
        # course indegree: [1, 0, 1, 0]
        
        # elements with in degree 0
        # DQueue = [3]
        # current_course = 1

        adj = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        result = []
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
    
        # add courses with 0 dependency to queue
        for i, in_degree in enumerate(indegree):
            if(in_degree == 0):
                q.append(i)
        
        # q is empty if there is a cycle
        while(q):
            course = q.pop()
            result.append(course)
            if(len(result) == numCourses):
                return result
            for dependent in adj[course]:
                indegree[dependent] -=1
                if(indegree[dependent] == 0):
                    q.append(dependent)
        return []

