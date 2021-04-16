from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

h = int (sys.argv[1]) if len(sys.argv) > 1 else 1.7

vertices = (
    (1, -1, -1),
    (-1, -1, -1),
    (-1, -1, 1),
    (1, h, -1),
    (-1, h, -1),
    (-1, h, 1)
)

lines = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5)
)

faces = (
    (0, 1, 2),
    (3, 4, 5),
    (0, 2, 3),
    (2, 3, 5),
    (1, 2, 4),
    (2, 4, 5),
    (0, 1, 3),
    (1, 3, 4)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 0),
    (1, 1, 0),
    (1, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    (0, 1, 1)
)

def prism():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i += 1
    glEnd()

    # glColor3fv((0, 0.5, 0))
    # glBegin(GL_LINES)
    # for line in lines:
    #     for vertex in line:
    #         glVertex3fv(vertices[vertex])
    # glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(3, 2, 4, 0)
    prism()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Prisma")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0)
glTranslatef(0.0, 0.0, -8)
glRotatef(45, 1, 1, 1)
glutTimerFunc(50, timer, 1)
glutMainLoop()