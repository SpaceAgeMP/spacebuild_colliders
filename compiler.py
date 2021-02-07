import subprocess
from os import path
from multiprocessing import Process
from math import floor

def comp(i, c):
    f = "src/icosphere_%d.smd" % i
    outf = "colliders/%d_00/icosphere_%d.mdl" % (floor(i / 100), i)
    if path.exists(outf):
        return

    qcfile = """
$modelname	"%s"
$body mybody	"%s"
$staticprop
$surfaceprop	combine_metal
$cdmaterials	"models\props"

$sequence idle	"%s"

$collisionmodel	"%s" { $concave $maxconvexpieces 400 }
""" % (outf, f, f, f)

    fh = open("compile_%d.qc" % c, "w")
    fh.write(qcfile)
    fh.close()

    subprocess.run(["studiomdl.exe", "compile_%d.gc" % c], capture_output=True)
    print("Done %d / %d" % (i, c))

MAX_PROC = 32

def runP(p):
    for i in range(p+1,6000,MAX_PROC):
        comp(i, p)

if __name__ == '__main__':
    procs = []
    for i in range(0, MAX_PROC):
        p = Process(target=runP, args=(i,))
        procs += [p]
        p.start()

    for p in procs:
        p.join()

    for i in range(1,4097):
        comp(i, 0)
