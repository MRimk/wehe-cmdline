import os, subprocess
def run_wehe_test(wehe_app, site='', results_dir='results'):
    
    command = [
        'java', '-jar', 'wehe-cmdline-4.0.0.jar', 
        '-n', wehe_app,
        # '-s', '128.179.209.156', # uncomment this line to run the client with the local server (machine in the Lab)
        '-m', 'https://locate-dot-mlab-sandbox.appspot.com/v2/nearest/wehe/replay', # this is the Locate service for the sandbox sites
        '-l', 'debug', 
        '-y', # comment/uncomment this line to run the localization test
        '-c', '-r', '{}/'.format(results_dir)]
    if site != '': # add sites that you want the locate service to see it
        command += ['-site', site]
    subprocess.run(command, timeout=300)
 
run_wehe_test('youtube')
sites = ['trn02', 'mil06', 'lis02', 'ord06', 'arn03', 'prg05', 'bom04', 'dfw03', 'syd03', 'tgd01'] # normal wehe sites all over the world (to try to create Y topos)
# sites = ['lga0t', 'lga1t', 'geg01'] # locate service sites to test them one by one
for i in range(1):
   for site in sites:
       print("\n\n\n\n\n\n=======================================================================\n\nRunning test for site:", site)
       run_wehe_test('youtube', site)
    
    
# differentiation is disabled (i.e. is normal)
# sites run 2025-08-27: 
#   'trn02', 'mil06', 'lis02', 'ord06', 'arn03', 'prg05', 'bom04', 'dfw03', 'syd03', 'tgd01' at time 12:15 local
#   4x 'trn02', 'mil06', 'lis02', 'ord06', 'arn03', 'prg05', 'bom04', 'dfw03', 'syd03', 'tgd01' at time 12:15-12:20 local

# all sites rerun with 194.230.158.71 ip at 12:00, 2025-08-28
