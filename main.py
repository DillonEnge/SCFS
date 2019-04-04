import argparse
import timelines
import micro_timeline_events as micro_events
from intra_personal import generate_birth_statistics
from lib import generate_initial_json, get_trait_tree

def main(generate_json, time_instances):
    print(f'Time instances: {time_instances}')
    print(f'Generate Json: {generate_json}')

    #TODO Dynamically load functions / events / timelines etc. based on configs
    timeline = timelines.BaseTimeline()
    timeline_function = micro_events.RandomEvent
    timeline.register_event(timeline_function)

    if generate_json:
        generate_initial_json()

    #TODO Generic generator - similar to generic events / timelines
    generate_birth_statistics()

    for _ in range(time_instances):
        timeline.step(get_trait_tree())
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '-timeinstances', dest='time_instances', type=int, default=10, help='Number of time instances to input into the time function')
    parser.add_argument('-generate_json_file', dest='generate_json_file', action='store_true')
    args = parser.parse_args()

    main(args.generate_json_file, args.time_instances)