class Solution:
    def hardestWorker(self, n: int, logs):
        len_logs = len(logs)
        
        max_duration = None
        employee_with_max_duration = None
        i = 0
        while (i < len_logs):
            if (i == 0):
                start_time = 0
                end_time = logs[i][1]
            else:
                start_time = logs[i-1][1]
                end_time = logs[i][1]
            if (max_duration is None or end_time - start_time >= max_duration):
                employee_with_max_duration = min(employee_with_max_duration, logs[i][0]) if max_duration == end_time - start_time else logs[i][0]
                max_duration = end_time - start_time
            i += 1

        return employee_with_max_duration