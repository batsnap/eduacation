#include <iostream>
#include <cstdlib>
#include <clocale>
#include <ctime>
#include <cmath>
#include <fstream>
using namespace std;
const int n = 4, m = 8;
ofstream fout("file.txt");

void FullfillMatrix(float** a) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) a[i][j] = -10 + rand() % (10 - (-10) + 1);
}

void PrintMatrix(float** a) {
	cout << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << a[i][j] << " " << "\t";
		}
		cout << endl;
	}
	cout << endl;
}

void FindPlusAverage(float** a) {
	int k = 0;
	float sum = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			if (a[i][j] >= 0) {
				k++;
				sum += a[i][j];
			}
		}
	cout << "\n среднее арифметическое = " << sum / k << endl;

	fout << "\n среднее арифметическое = " << sum / k << endl;

}

void CountPlusNumberInEachLine(float** a) {
	int k;

	fout << "\n количество неотрицательных элементов в каждой строке:" << endl << endl;

	cout << "\n количество неотрицательных элементов в каждой строке:" << endl << endl;
	for (int i = 0; i < n; i++) {
		cout << "\n в строке #" << i + 1 << "таких элементов " << k;
		fout << "\n в строке #" << i + 1 << "таких элементов " << k;
		k = 0;
		for (int j = 0; j < m; j++) if (a[i][j] >= 0) k++;
	}

}

void FullfillSettingArray(float** a) {
	cout << "\n массив из 0 и 1 по заданному условию" << endl << endl;
	int f;
	float* b = new float[m];
	for (int i = 0; i < n; i++) {
		f = 1;
		for (int j = 0; j < m; j++) if (a[i][i] < a[i][j]) f = 0;
		b[i] = f;
		cout << " | " << b[i] << " | ";
	}
	cout << endl;
}

void SumMatrix(float** a) {
	int sum = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) sum += a[i][j];
	cout << "\n сумма элементов матрицы = " << sum << endl;
}

void ChangeToAbsPartOfMatrix(float** a) {
	cout << "\n матрица с абослютными значениями элементов, выше главной диагонали:" << endl;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) if (i < j) a[i][j] = abs(a[i][j]);
	PrintMatrix(a);
}

void SumMainDiagonal(float** a) {
	cout << "\n сумма элементов главной диагонали матрицы = ";
	int sum = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) if (i = j) sum += a[i][j];
	cout << sum << endl;
}

int main() {
	setlocale(LC_ALL, "Russian");
	srand(time(NULL));

	float** a=new float* [n];
	for (int i = 0; i < n; i++) a[i] = new float[m];
	PrintMatrix(a);

	
	fout << "Работа с файлами в С++"; // запись строки в файл
	FindPlusAverage(a);
	CountPlusNumberInEachLine(a);

	fout.close();

	FullfillSettingArray(a);
	SumMatrix(a);
	ChangeToAbsPartOfMatrix(a);
	SumMainDiagonal(a);
	system("pause");
	return 0;
}