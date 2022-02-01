class UtilityCore:
    @staticmethod
    def is_lst_ascending(lst):
        s_lst = sorted(lst)
        print(s_lst, lst)
        if s_lst == lst:
            return True
        else:
            return False

    @staticmethod
    def is_lst_contain_same_data(lst):
        if len(set(lst)) == 1:
            return True
        else:
            return False


