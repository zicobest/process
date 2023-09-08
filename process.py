import pandas as pd


def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=',')
    num_events = len(event_log)
    num_case = len(event_log.case_id.unique())  # to avoid repetition
    print("Number of events{}\n number of cases:{}".format(num_events, num_case))


if __name__ == "__main__":
    import_csv("p2p_event_log.csv")
    print(pd.read_csv("p2p_event_log.csv"))
