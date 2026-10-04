class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # numCourses from 0 to numCourses - 1
        # in prereqs: [ai,bi] must take course b to take course a
        # find the ordering yo ushould take to finish all courses
        # create an adj list
        # the prereqs needed to take this course
        # if you want to take this course you'll have to take the prereqs to it
        # dfs sorta stuff
        adjList = [[] for i in range(0, numCourses)]

        for prereq in prerequisites:
            take, req = prereq[0],prereq[1]

            adjList[take].append(req)
        
        # if in the adjList it's empty (no prereqs) then we can take that course

        # the only case in which we wont be able to take it is in a cycle,
        # so we just need to check for a cycle while putting in courses we take
        order = []
        coursesTaken = set()
        seen = set()

        def dfsCanTake(curCourse):
            if len(adjList[curCourse]) == 0:
                if curCourse not in coursesTaken:
                    coursesTaken.add(curCourse)
                    order.append(curCourse)
                return True # obv can take it no prereqs
            if curCourse in seen:
                return False
            seen.add(curCourse)
            # if we can take the prereqs then we can take the course
            for prereq in adjList[curCourse]:
                if not dfsCanTake(prereq):
                    return False
            seen.remove(curCourse)
            adjList[curCourse] = [] # get rid of the prereqs since we can take it. Already taken the prereqs
            if curCourse not in coursesTaken:
                coursesTaken.add(curCourse)
                order.append(curCourse)
            return True
        
        for i in range(0, numCourses):
            if not dfsCanTake(i):
                return []
        return order