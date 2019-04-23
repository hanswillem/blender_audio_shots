'''
Exports audio clips seperated by markers
'''

import bpy

def main_openFolder():
    import subprocess
    subprocess.Popen('explorer ' + bpy.path.abspath('//'))

def main_getMarkerNameOfFrame(f):
    # make a dictionary of marker framenumbers and marker names
    d_mrks = {}
    for i in  bpy.context.scene.timeline_markers:
        d_mrks[i.frame] = i.name
    # make a list of the frame numbers and sort them
    mrks = [marker.frame for marker in bpy.context.scene.timeline_markers]
    mrks.sort()
    # get the marker name and return it
    for i in range(len(mrks) - 1):
        if mrks[i] <= f < mrks[i + 1]:
            return  d_mrks[mrks[i]];


def main_exportAudioShots():
    rng_start = bpy.context.scene.frame_start
    rng_end = bpy.context.scene.frame_end
    mrks = [marker.frame for marker in bpy.context.scene.timeline_markers]
    mrks.sort()
    for i in range(len(mrks) - 1):
        bpy.context.scene.frame_start = mrks[i]
        bpy.context.scene.frame_end = mrks[i + 1] - 1  
        bpy.ops.sound.mixdown(filepath = bpy.path.abspath('//') + str(main_getMarkerNameOfFrame(mrks[i])) + '.wav', container='WAV', codec = 'PCM')
    #reset frame range
    bpy.context.scene.frame_start = rng_start
    bpy.context.scene.frame_end = rng_end
    main_openFolder()
    

main_exportAudioShots()
