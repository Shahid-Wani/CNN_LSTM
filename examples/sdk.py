# Install the Lightning SDK
# pip install -U lightning-sdk

# login to the platform
# export LIGHTNING_USER_ID=a88c3199-3656-43bd-9878-807faff0693f
# export LIGHTNING_API_KEY=adb513c4-77d4-4c9a-991f-86dac293ac07

from lightning_sdk import Machine, Studio, JobsPlugin, MultiMachineTrainingPlugin

# Start the studio
s = Studio(name="my-sdk-studio", teamspace="language-model", org="2018014204danish", create_ok=True)
print("starting Studio...")
s.start()

# prints Machine.CPU-4
print(s.machine)

print("switching Studio machine...")
s.switch_machine(Machine.A10G)

# prints Machine.A10G
print(s.machine)

# prints Status.Running
print(s.status)

print(s.run("nvidia-smi"))

print("Stopping Studio")
s.stop()

# duplicates Studio, this will also duplicate the environment and all files in the Studio
duplicate = s.duplicate()

# delete original Studio, duplicated Studio is it's own entity and not related to original anymore
s.delete()

# stop and delete duplicated Studio
duplicate.stop()
duplicate.delete()
    