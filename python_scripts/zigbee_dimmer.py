##########################################################
# LIGHT DIMMER PACKAGE BY MARCO REALACCI @ HASSIOHELP.EU #
#   for any question write to: marco@marcorealacci.me    #
##########################################################

######################## CODE ####################################################################################

lights = data.get('lights')
is_stop = False
if data.get('direction') == 'stop':
    is_stop = True
speed = data.get('speed')
direction = data.get('direction')
if direction == 'down':
    speed = speed * -1
if direction == 'auto':
    if hass.states.get('input_boolean.d_dimmer_way').state == 'off':
        hass.services.call('input_boolean', 'turn_on', {'entity_id': 'input_boolean.d_dimmer_way'}, False)
    else:
        hass.services.call('input_boolean', 'turn_off', {'entity_id': 'input_boolean.d_dimmer_way'}, False)
    for l in data.get('ha_lights'):
        b = hass.states.get(l).attributes.get('brightness')
        if b > 240:
            hass.services.call('input_boolean', 'turn_off', {'entity_id': 'input_boolean.d_dimmer_way'}, False)
        if b < 30:
            hass.services.call('input_boolean', 'turn_on', {'entity_id': 'input_boolean.d_dimmer_way'}, False)
    time.sleep(0.2)
    if hass.states.get('input_boolean.d_dimmer_way').state == 'off':
        speed = speed * -1

if is_stop:
    for light in lights:
        service_data = {'topic': 'zigbee2mqtt/' + light + "/set", 'payload': '{"brightness_move": "stop"}'}
        hass.services.call('mqtt', 'publish', service_data, False)
else:
    for light in lights:
        service_data = {'topic': 'zigbee2mqtt/' + light + "/set", 'payload': '{"brightness_move": ' + str(speed) + '}'}
        hass.services.call('mqtt', 'publish', service_data, False)

##################################################################################################################