from collections import defaultdict
import re

class Solution:
    def countDaysTogether(self, arrive_alice, leave_alice, arrive_bob, leave_bob):
        def get_count_days_of_month_map(is_leap_year):
            count_days_of_month_map = defaultdict(int)
            count_days_of_month_map[1] = 31
            if (is_leap_year):
                count_days_of_month_map[2] = 29
            else:
                count_days_of_month_map[2] = 28
            count_days_of_month_map[3] = 31
            count_days_of_month_map[4] = 30
            count_days_of_month_map[5] = 31
            count_days_of_month_map[6] = 30
            count_days_of_month_map[7] = 31
            count_days_of_month_map[8] = 31
            count_days_of_month_map[9] = 30
            count_days_of_month_map[10] = 31
            count_days_of_month_map[11] = 30
            count_days_of_month_map[12] = 31

            return count_days_of_month_map

        def get_month_and_date(mm_dd):
            match = re.match('([0-9]{2})\-([0-9]{2})', mm_dd)
            if (match):
                arrive_alice_month, arrive_alice_day = match.groups()
                arrive_alice_month = int(arrive_alice_month)
                arrive_alice_day = int(arrive_alice_day)

                return (arrive_alice_month, arrive_alice_day)

        def get_sum_days_from_1_1(mm_dd):
            match = re.match('([0-9]{2})\-([0-9]{2})', mm_dd)
            if (match):
                arrive_month, arrive_day = match.groups()
                arrive_month = int(arrive_month)
                arrive_day = int(arrive_day)

                month_1_1 = 1

                sum_days_from_1_1 = 0

                count_days_of_month_map = get_count_days_of_month_map(False)
                m = month_1_1
                
                while (m < arrive_month):
                    sum_days_from_1_1 += count_days_of_month_map[m]
                    m += 1

                sum_days_from_1_1 += arrive_day

                return sum_days_from_1_1
        
        sum_days_from_1_1_to_arrive_alice = get_sum_days_from_1_1(arrive_alice)
        sum_days_from_1_1_to_leave_alice = get_sum_days_from_1_1(leave_alice)
        sum_days_from_1_1_to_arrive_bob = get_sum_days_from_1_1(arrive_bob)
        sum_days_from_1_1_to_leave_bob = get_sum_days_from_1_1(leave_bob)

        if (get_month_and_date(arrive_alice) <= get_month_and_date(arrive_bob) <= get_month_and_date(leave_alice) <= get_month_and_date(leave_bob)):
            return sum_days_from_1_1_to_leave_alice - sum_days_from_1_1_to_arrive_bob + 1
        elif (get_month_and_date(arrive_alice) <= get_month_and_date(leave_alice) < get_month_and_date(arrive_bob) <= get_month_and_date(leave_bob)):
            return 0
        elif (get_month_and_date(arrive_bob) <= get_month_and_date(leave_bob) < get_month_and_date(arrive_alice) <= get_month_and_date(leave_alice)):
            return 0
        elif (get_month_and_date(arrive_bob) <= get_month_and_date(arrive_alice) <= get_month_and_date(leave_alice) <= get_month_and_date(leave_bob)):
            return sum_days_from_1_1_to_leave_alice - sum_days_from_1_1_to_arrive_alice + 1
        elif (get_month_and_date(arrive_bob) <= get_month_and_date(arrive_alice) <= get_month_and_date(leave_bob) <= get_month_and_date(leave_alice)):
            return sum_days_from_1_1_to_leave_bob - sum_days_from_1_1_to_arrive_alice + 1
        elif (get_month_and_date(arrive_alice) <= get_month_and_date(arrive_bob) <= get_month_and_date(leave_bob) <= get_month_and_date(leave_alice)):
            return sum_days_from_1_1_to_leave_bob - sum_days_from_1_1_to_arrive_bob + 1