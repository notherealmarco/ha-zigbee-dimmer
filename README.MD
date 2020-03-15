# Zigbee dimmer
### Dim zigbee lights natively from Home Assistant

## Configuration
It's all based on the `python_script.zigbee_dimmer` service

```
lights:
  - '0x14b457fffe6792fa' #zigbee2mqtt device id or friendly name
ha_lights:
  - 'light.mrc_spotlight_01' #Home Assistant entity_id
direction: 'up' #can be up, down and stop
speed: 80 #the dimming speed
```