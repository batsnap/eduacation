#define GL_SILENCE_DEPRECATION
#include "math.h"
#include <GLUT/glut.h>
void Display()
{
	glClearColor(1.0f,1.0f,1.0f,1.0f);
    glBegin(GL_QUADS);
    	GLUquadricObj *q = gluNewQuadric();
		gluQuadricDrawStyle(q, GLU_FILL);
		glColor3f(0.0f, 0.0f, 0.0f);
		gluCylinder(q, radius, 0, height, segments_count, segments_count);
		gluDeleteQuadric(q);
    glEnd();
/*
	glBegin(GL_QUADS);
    	glColor3f(0.0f,0.f,0.0f); 
    	glVertex2f(0.304f,0.3f);
    	glVertex2f(0.304f,-0.304f);
    	glVertex2f(-0.304f,-0.304f);
    	glVertex2f(-0.304f,0.3f);
    glEnd();

    glBegin(GL_QUADS);
    	glColor3f(1.0f,0.f,1.0f); 
    	glVertex2f(0.3f,0.3f);
    	glVertex2f(0.3f,-0.3f);
    	glVertex2f(-0.3f,-0.3f);
    	glVertex2f(-0.3f,0.3f);
    glEnd();

	glBegin(GL_QUADS);
    	glColor3f(0.0f,0.9f,0.999f); 
    	glVertex2f(0.2f,0.2f);
    	glVertex2f(0.2f,-0.2f);
    	glVertex2f(-0.2f,-0.2f);
    	glVertex2f(-0.2f,0.2f);
    glEnd();
    glBegin(GL_QUADS);
    	glColor3f(1.0f,1.0f,1.f); 
    	glVertex2f(0.1f,0.1f);
    	glVertex2f(0.1f,-0.1f);
    	glVertex2f(-0.1f,-0.1f);
    	glVertex2f(-0.1f,0.1f);
    glEnd();
    */
	glutSwapBuffers();
}

void Initialize()
{
	glClearColor(1, 1, 1, 0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-1, 1, -1, 1, 0, 0);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE);
	glutInitWindowSize(400, 400);
	glutInitWindowPosition(100, 200);
	glutCreateWindow("SALAD");
	glutDisplayFunc(Display);
	Initialize();
	glutMainLoop();

	return 0;
}