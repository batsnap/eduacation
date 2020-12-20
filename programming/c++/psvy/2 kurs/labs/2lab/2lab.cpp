#define GL_SILENCE_DEPRECATION
#include "math.h"
#include <GLUT/glut.h>
float base_x, base_y, base_z, sdv_x, sdv_y;
void flower()
{

	glTranslatef(0.,0.,0.039);
	glColor3f(1.0f, 1.0f, 0.0f);
	glutSolidSphere(0.15, 1000, 1000);
	glColor3f(1.0f, 1.0f, 0.0f);
	glutSolidSphere(0.15, 1000, 1000);
	glTranslatef(0.,0.,-0.039);

	glTranslatef(0.2,0.,0.);
	glColor3f(1.0f, 0.0f, 0.0f);
	glutSolidSphere(0.1, 1000, 1000);

	glTranslatef(-0.2,0.,0.);

	glTranslatef(-0.2,0.0,0.);
	glutSolidSphere(0.1, 1000, 1000);

	glTranslatef(0.2,0.,0.);

	glTranslatef(0.,0.2,0.);
	glutSolidSphere(0.1, 1000, 1000);

	glTranslatef(0.,-0.2,0.);

	glTranslatef(0.0,-0.2,0.);
	glutSolidSphere(0.1, 1000, 1000);
	
	glTranslatef(0.,0.2,0.);

	glTranslatef(0.15,0.15,0.);
	glutSolidSphere(0.1, 1000, 1000);
	
	glTranslatef(-0.15,-0.15,0.);

	glTranslatef(-0.15,0.15,0.);
	glutSolidSphere(0.1, 1000, 1000);
	
	glTranslatef(0.15,-0.15,0.);

	glTranslatef(0.15,-0.15,0.);
	glutSolidSphere(0.1, 1000, 1000);
	
	glTranslatef(-0.15,0.15,0.);

	glTranslatef(-0.15,-0.15,0.);
	glutSolidSphere(0.1, 1000, 1000);
	
	glTranslatef(0.15,0.15,0.);

	glEnd();
}
//Инициализировать 3D
void initRendering() {
	glClearColor(0.7, 0.7, 0.7, 0);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_LIGHT1);
	glEnable(GL_NORMALIZE);
	glShadeModel(GL_SMOOTH);
}

void handleResize(int w, int h) {
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45.0, (double)w / (double)h, 1.0, 200.0);
}

void drawScene() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0.0f, 0.0f, -13.0f);

	//Добавление света
	GLfloat ambientColor[] = { 0.4f, 0.4f, 0.4f, 1.0f };
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambientColor);
	GLfloat lightColor0[] = { 0.5f, 0.5f, 0.5f, 1.0f };
	GLfloat lightPos0[] = { 1.0f, -8.0f, 8.0f, 1.0f };
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor0);
	glLightfv(GL_LIGHT0, GL_POSITION, lightPos0);
	GLfloat lightColor1[] = { 0.0f, 0.2f, 0.2f, 0.5f };
	GLfloat lightPos1[] = { -1.0f, 0.5f, 0.5f, 0.0f };
	glLightfv(GL_LIGHT1, GL_DIFFUSE, lightColor1);
	glLightfv(GL_LIGHT1, GL_POSITION, lightPos1);

	glTranslatef(base_x, base_y, base_z);
	glRotatef(sdv_x, 1.0f, 0.0f, 0.0f);
	glRotatef(sdv_y, 0.0f, 1.0f, 0.0f);

	glRotatef(1, 1.0f, 0.0f, 0.0f);
	glRotatef(-1, 0.0f, 0.0f, 1.0f);

	glBegin(GL_QUADS);

	glColor3f(1.0f, .5f, 0.f);
    glutSolidCone(0.01, 0.01, 1000, 1000);
    glRotated(90, 0, 0, 1);
    glRotated(-90, 0, 1, 0);
    glColor3f(1.0f, 0.5f, 0.f);
    glutSolidCone(1.5, 4.5, 1000, 1000);
	
	glTranslatef(0.,0.,-0.15);

	glTranslatef(0.9,0.9,0);
	flower();
	glTranslatef(-0.9,-0.9,0);

	glTranslatef(-0.9,-0.9,0);
	flower();
	glTranslatef(0.9,0.9,0);

	glTranslatef(-0.9,0.9,0);
	flower();
	glTranslatef(0.9,-0.9,0);

	glTranslatef(0.9,-0.9,0);
	flower();
	glTranslatef(-0.9,0.9,0);


	glTranslatef(0.,1.2,0);
	flower();
	glTranslatef(0.,-1.2,0);

	glTranslatef(0.,-1.2,0);
	flower();
	glTranslatef(0.,1.2,0);

	glTranslatef(1.2,0.,0);
	flower();
	glTranslatef(-1.2,0.,0);

	glTranslatef(-1.2,0.,0);
	flower();
	glTranslatef(1.2,0.,0);



	glTranslatef(0.45,0.45,0);
	flower();
	glTranslatef(-0.45,-0.45,0);

	glTranslatef(-0.45,-0.45,0);
	flower();
	glTranslatef(0.45,0.45,0);

	glTranslatef(-0.45,0.45,0);
	flower();
	glTranslatef(0.45,-0.45,0);

	glTranslatef(0.45,-0.45,0);
	flower();
	glTranslatef(-0.45,0.45,0);


	glTranslatef(0.,0.7,0);
	flower();
	glTranslatef(0.,-0.7,0);

	glTranslatef(0.,-0.7,0);
	flower();
	glTranslatef(0.,0.7,0);

	glTranslatef(0.7,0.,0);
	flower();
	glTranslatef(-0.7,0.,0);

	glTranslatef(-0.7,0.,0);
	flower();
	glTranslatef(0.7,0.,0);

	flower();


	glEnd();

	glutSwapBuffers();
}

//Для клавиш
void KeyboardEventBut(unsigned char key, int a, int b)
{
	switch (key)
	{
	case 119: base_y += 0.3f; break; //W - сдвиг наверх
	case 115: base_y -= 0.3f; break; //S - сдвиг вниз
	case 97: base_x -= 0.3f; break; //A - сдвиг влево
	case 100: base_x += 0.3f; break; //D - сдвиг вправо
	case 113: base_z += 1.3f; break; //Q - приблизить
	case 101: base_z -= 1.3f; break; //E - отдалить
	}
	glutPostRedisplay();
}

//Для стрелок
void KeyboardEvent(int key, int a, int b)
{
	switch (key)
	{
	case 102: sdv_y -= 10.f; break; //стрелка вправо - поворот по часовой
	case 100: sdv_y += 10.f; break; //стрелка влево - поворот против часовой
	case 101: sdv_x += 10.f; break; //стрелка вверх - поворот по вертикали против часовой
	case 103: sdv_x -= 10.f; break; //стрелка вниз - поворот по вертикали по часовой
	}

	if (sdv_y > 360) {
		sdv_y -= 360;
	}

	if (sdv_x > 360) {
		sdv_x -= 360;
	}
	glutPostRedisplay();
}


int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(650, 650);

	glutCreateWindow("Букет");
	initRendering();

	glutDisplayFunc(drawScene);
	glutReshapeFunc(handleResize);
	glutKeyboardFunc(*KeyboardEventBut);
	glutSpecialFunc(KeyboardEvent);

	glutMainLoop();
	return 0;
}
