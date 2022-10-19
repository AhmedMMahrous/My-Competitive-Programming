from pickletools import int4


with open(r'200+ Exercises  Programming in Python\13- reading files\Ex 3 playway.csv' ,'r') as file:
    content = file.read().splitlines()


 
volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(vol) for vol in volumes]
max_vol = max(volumes)
print(f'Max Vol: {max_vol}')

