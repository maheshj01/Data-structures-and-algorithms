### Problem 207. Course Schedule (Medium): https://leetcode.com/problems/course-schedule/

### tags: graph, topological `sort, DFS, BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        visited = set()
        for course, pre in prerequisites:
            if(course not in prereq):
                prereq[course] = [pre]
            else:
                prereq[course].append(pre)
        
        for i in range(numCourses):
            if(i not in prereq):
                prereq[i] = []

        def take_course_dfs(c):
            # loop
            if(c in visited):
                return False
            # no prerequisite
            if(len(prereq[c]) == 0):
                return True
            visited.add(c)
            for p in prereq[c]:
                if(not take_course_dfs(p)):
                    return False
            visited.remove(c)
            prereq[c] = []
            return True

        for course in range(numCourses):
            if(not take_course_dfs(course)):
                return False
        return True
    
    
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
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
        courses_completed = 0
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
            courses_completed += 1
            if(courses_completed == numCourses):
                return True
            for dependent in adj[course]:
                indegree[dependent] -=1
                if(indegree[dependent] == 0):
                    q.append(dependent)

        return False

