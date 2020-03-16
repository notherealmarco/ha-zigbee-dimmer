# Zigbee dimmer
### Dim zigbee2mqtt lights natively from Home Assistant

## Installation
1. Copy `python_scripts/zigbee_dimmer.py` into `<your Home Assistant config folder>/python_scripts`

2. Add `python_script:` in your configuration.yaml (if you haven't done it already)

3. Add this in your configuration.yaml:
```
input_boolean:
  d_dimmer_way:
    name: d_dimmer_way
```

4. Restart Home Assistant, or call `python_script.reload` if the component is already enabled.

## Usage
Call the `python_script.zigbee_dimmer` service

##### Service data:
```
lights:
  - '0x14b457fffe6792fa' #zigbee2mqtt device id or friendly name
ha_lights:
  - 'light.mrc_spotlight_01' #Home Assistant entity_id
direction: 'up' #can be up, down, auto and stop
speed: 80 #the dimming speed
```

| key | value |
|------------|----------------------------------------------------------------------------|
| lights | array with the zigbee2mqtt lights (id or friendly name) |
| ha_lights | array with the home assistant's entity_ids |
| direction | can be 'up' to increase the brightness, 'down' to decrease it, 'auto' to automatically detect and 'stop' to stop the dimmer and update the entity attributes on Home Assistant |
| speed | the dimming speed, 80 is a good value |
