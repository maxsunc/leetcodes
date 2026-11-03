class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # must take num courses from 0 to numCourses - 1

        # only false if we detect a cycle
        # [1,0] => must take course 0 before taking course 1

        prereqs = [[] for i in range(0,numCourses)]

        for p in prerequisites:
            req = p[1]
            course = p[0]
            prereqs[course].append(req)
        

        # graph to check if cycle
        # dfs
        seen = set()
        def canTakeDfs(curCourse):
            if len(prereqs[curCourse]) == 0:
                return True
            
            if curCourse in seen:
                return False
            # here there are prereqs for this course
            seen.add(curCourse)
            
            for prereq in prereqs[curCourse]:
                if not canTakeDfs(prereq):
                    return False
            prereqs[curCourse].clear()
            seen.remove(curCourse)
            return True

        for c in range(0,numCourses):
            if not canTakeDfs(c):
                return False
        return True