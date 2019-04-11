import argparse
import timelines
import micro_timeline_events as micro_events
from lib import TraitTreeModifier
from intra_personal import initialize_character

def main(manual_step_through, population_size, time_instances):
    write_config(manual_step_through, population_size, time_instances)
    
    #TODO Dynamically load functions / events / timelines etc. based on configs
    timeline = timelines.BaseTimeline()
    timeline.register_event(micro_events.AgeEvent)
    timeline.register_event(micro_events.MidlifeCrisisEvent)
    population = []

    for p in range(population_size):
        population.append(initialize_character(f'NamePlaceHolder_{p}'))

    for _ in range(time_instances):
        if(manual_step_through):
            input("\nPress Enter to continue...")
        timeline.step(population)

def write_config(manual_step_through, population_size, time_instances):
    print('Config')
    print('---------------------------')
    print(f'Time instances: {time_instances}')
    print(f'Population Size: {population_size}')
    print(f'Manual Step Through: {manual_step_through}')
    print('---------------------------\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '-timeinstances', dest='time_instances', type=int, default=10, help='Number of time instances to input into the time function')
    parser.add_argument('-p', '-population', dest='population_size', type=int, default=1, help='Number of people in the population')
    parser.add_argument('-m', dest='manual_step_through', action='store_true')
    args = parser.parse_args()

    main(args.manual_step_through, args.population_size, args.time_instances)
