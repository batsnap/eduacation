#define GL_SILENCE_DEPRECATION
#include "math.h"
#include <GLUT/glut.h>
void Display()
{
	glClearColor(1.0f,1.0f,1.0f,1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    glBegin(GL_QUADS);
        glColor3f(0.5f,0.5f,0.5f); 
        glVertex2f(0.5f,0.5f);
        glVertex2f(0.5,-0.5f);
        glVertex2f(-0.5f,-0.5f);
        glVertex2f(-0.5f,0.5f);
    glEnd();

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
	glutSwapBuffers();
}

void Initialize()
{
	glClearColor(0,0,0,0);
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
	glutCreateWindow("KVADRAT");
	glutDisplayFunc(Display);
	Initialize();
	glutMainLoop();

	return 0;
}
/*/*
    //1 шар
    glTranslated(0, 10, 0);
    glColor3f(1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.8, 100, 100);

    //Нос
    glTranslated(0, 0, 1);
    glColor3f(1.0f, 0.3f, 0.f);
    glutSolidCone(0.2, 1.2, 10, 100);
*/
/*
    //Глаза
    glTranslated(0.2, 0.3, -0.2);
    glColor3f(0.05f, 0.05f, 0.05f);
    glutSolidCone(0.1, 0.3, 10, 100);
    glTranslated(-0.4, 0, 0);
    glutSolidCone(0.1, 0.3, 10, 100);

    //2 шар
    glTranslated(0.2, -1.8, -0.6);
    glColor3f(1.0f, 1.0f, 1.0f);
    glutSolidSphere(1.1, 100, 100);

    //1 рука
    glTranslated(1.1, 0, 0);
    glColor3f(1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.35, 100, 100);

    //2 рука
    glTranslated(-2.2, 0, 0);
    glColor3f(1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.35, 100, 100);

    //3 шар
    glTranslated(1.1, -2.2, 0);
    glColor3f(1.0f, 1.0f, 1.0f);
    glutSolidSphere(1.5, 100, 1000);
    glTranslated(0, 4.3, 0);
    
    glColor3f(1.0f, 1.0f, 0.f);
    glutSolidCone(0.01, 0.01, 1000, 1000);
    glRotated(90, 0, 0, 1);
    glRotated(-90, 0, 1, 0);
    glColor3f(1.0f, 1.0f, 0.f);
    glutSolidCone(1.5, 4.5, 1000, 1000);
    glRotated(90, 0, 0, 1);
    glRotated(-90, 0, 1, 0);
    glColor3f(1.0f, 0.0f, 0.f);
    glutSolidSphere(0.1, 1000, 1000);*/
    //Шляпа
