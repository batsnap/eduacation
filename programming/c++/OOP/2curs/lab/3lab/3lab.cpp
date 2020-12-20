/*В программе Win32->Win32Project в функции WndProc 
вставить обработчик события
case WM_CREATE: { break;}
В нем создать две фигуры типа окружности и прямоугольника и положить их в общее 
глобальное хранилище, применяя контейнер vector. (Использовать следует конструктор 
с необходимыми параметрами для каждого типа)
Далее в функции WndProc, в обработке события WM_PAINT, между строками
hdc = BeginPaint(hWnd, &ps);
и
EndPaint(hWnd, &ps);
последовательно проходя по хранимым в контейнере vectorданными, осуществить 
рисование окружности и прямоугольника.
*/

#include <vector>
#include "framework.h"
#include "Win32.h"

#define MAX_LOADSTRING 100

// Глобальные переменные:
HINSTANCE hInst;                                // текущий экземпляр
WCHAR szTitle[MAX_LOADSTRING];                  // Текст строки заголовка
WCHAR szWindowClass[MAX_LOADSTRING];            // имя класса главного окна

// Отправить объявления функций, включенных в этот модуль кода:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);

class Inventory
{
public:
    int left;
    int top;
    int right;
    int bottom;
    Inventory() {}
    virtual ~Inventory() {}
    virtual void paint(HDC hdc) {}
};

class Сircle : public Inventory
{
public:
    Сircle() {}
    Сircle(int x_1, int y_1, int x_2, int y_2) : Inventory()
    {
        left = x_1;
        top = y_1;
        right = x_2;
        bottom = y_2;
    }
    ~Сircle() {}
    void paint(HDC hdc)
    {
        Ellipse(hdc, left, top, right, bottom);
    }
};

class Rectangle_1 : public Inventory
{
public:

    Rectangle_1() {}
    Rectangle_1(int x_1, int y_1, int x_2, int y_2) : Inventory()
    {
        left = x_1;
        top = y_1;
        right = x_2;
        bottom = y_2;
    }
    ~Rectangle_1() {}
    void paint(HDC hdc)
    {
        Rectangle(hdc, left, top, right, bottom);
    }
};

std::vector<Inventory*> vec;

int APIENTRY wWinMain(_In_ HINSTANCE hInstance,
    _In_opt_ HINSTANCE hPrevInstance,
    _In_ LPWSTR lpCmdLine,
    _In_ int nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: Разместите код здесь.

    // Инициализация глобальных строк
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_WIN32, szWindowClass, MAX_LOADSTRING);
    MyRegisterClass(hInstance);

    // Выполнить инициализацию приложения:
    if (!InitInstance(hInstance, nCmdShow))
    {
        return FALSE;
    }

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_WIN32));

    MSG msg;

    // Цикл основного сообщения:
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    return (int)msg.wParam;
}



ATOM MyRegisterClass(HINSTANCE hInstance)
{
    WNDCLASSEXW wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc = WndProc;
    wcex.cbClsExtra = 0;
    wcex.cbWndExtra = 0;
    wcex.hInstance = hInstance;
    wcex.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(IDC_WIN32));
    wcex.hCursor = LoadCursor(nullptr, IDC_ARROW);
    wcex.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wcex.lpszMenuName = MAKEINTRESOURCEW(IDC_WIN32);
    wcex.lpszClassName = szWindowClass;
    wcex.hIconSm = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    return RegisterClassExW(&wcex);
}



BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
    hInst = hInstance; // Сохранить маркер экземпляра в глобальной переменной

    HWND hWnd = CreateWindowW(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, nullptr, nullptr, hInstance, nullptr);

    if (!hWnd)
    {
        return FALSE;
    }

    ShowWindow(hWnd, nCmdShow);
    UpdateWindow(hWnd);

    return TRUE;
}


LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    static int sx, sy;
    switch (message)
    {
    case WM_SIZE:
    {
        sx = LOWORD(lParam);
        sy = HIWORD(lParam);
    }
    break;
    case WM_CREATE:
    {
        vec.push_back(new Rectangle_1(300, 400, sy + 10, sy + 10));
        vec.push_back(new Сircle(200, 200, sy + 10, sy + 10));

    }
    break;
    case WM_COMMAND:
    {
        int wmId = LOWORD(wParam);
        // Разобрать выбор в меню:
        switch (wmId)
        {
        case IDM_ABOUT:
            DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
            break;
        case IDM_EXIT:
            DestroyWindow(hWnd);
            break;
        default:
            return DefWindowProc(hWnd, message, wParam, lParam);
        }
    }
    break;
    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hWnd, &ps);
        for (int i = 0; i < vec.size(); i++)
        {
            vec[i]->paint(hdc);
        }
        EndPaint(hWnd, &ps);
    }
    break;
    case WM_DESTROY:
    {
        for (int i = 0; i < vec.size(); i++)
        {
            delete vec[i];
        }
        PostQuitMessage(0);
    }
    break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

// Обработчик сообщений для окна "О программе".
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}
