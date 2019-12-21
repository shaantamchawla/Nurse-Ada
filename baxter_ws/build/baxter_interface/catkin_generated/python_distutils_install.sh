#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/scratch/shared/baxter_ws/src/baxter_interface"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/scratch/shared/baxter_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/scratch/shared/baxter_ws/install/lib/python2.7/dist-packages:/scratch/shared/baxter_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/scratch/shared/baxter_ws/build" \
    "/usr/bin/python" \
    "/scratch/shared/baxter_ws/src/baxter_interface/setup.py" \
    build --build-base "/scratch/shared/baxter_ws/build/baxter_interface" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/scratch/shared/baxter_ws/install" --install-scripts="/scratch/shared/baxter_ws/install/bin"
