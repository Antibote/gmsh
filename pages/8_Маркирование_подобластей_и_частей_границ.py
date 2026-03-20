import streamlit as st

st.set_page_config(page_title="✏️", layout="wide")


def show_code(code, language="python"):
    st.code(code, language=language)


sections = {
    "Физические группы": "",
    "Пример 1-D": "",
    "Пример 2-D": "",
    "Пример 3-D": "",
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))
st.write("""##### Маркирование подобластей и частей границ""")

if choice == "Физические группы":
    st.markdown("##### Физические группы")
    st.markdown(
        """
        **Физические группы** — это именованные или помеченные тегом наборы геометрических объектов,
        используемые для логического выделения частей модели в Gmsh. Они позволяют связывать геометрию с расчётным смыслом:
        выделять границы, области, подобласти, интерфейсы и другие элементы, которые затем используются при постановке
        численной задачи

        Физические группы могут относиться к объектам разной размерности: кривым, поверхностям и объёмам.
        Каждая такая группа служит меткой для геометрических объектов и используется при передаче модели в расчётные пакеты
        для назначения граничных условий, материалов и других свойств
        """
    )

    st.markdown("##### Команды выделения физических групп")
    st.markdown(
        """
        Для создания физических групп используются команды `Physical Curve`, `Physical Surface`, `Physical Volume`.

        **`Physical Curve`**  
        Помечает линии и кривые как физические группы. Используется для выделения одномерных границ и контуров модели,
        на которых в дальнейшем могут задаваться различные условия расчёта

        **`Physical Surface`**  
        Помечает поверхности как физические группы. Используется для выделения двумерных областей модели или граничных
        поверхностей в трёхмерных задачах

        **`Physical Volume`**  
        Помечает объёмы как физические группы. Используется в трёхмерных моделях для выделения расчётных областей,
        подобластей и частей геометрии с различными свойствами
        """
    )

elif choice == "Пример 1-D":
    st.markdown("##### Пример 1-D")

    geo_code_1d = """
SetFactory("OpenCASCADE");

// Создаем квадрат
Rectangle(1) = {0, 0, 0, 1, 1};

// Физические группы (граничные условия)
Physical Curve("Fixed_Boundary") = {4};
Physical Curve("Heat_Flux") = {2};
Physical Surface("Domain") = {1};

// Генерация сетки
Mesh.CharacteristicLengthMin = 0.1;
Mesh 2;
"""
    show_code(geo_code_1d, "python")

elif choice == "Пример 2-D":
    st.markdown("##### Пример 2-D")

    geo_code_2d = """
SetFactory("OpenCASCADE");

// Первый прямоугольник (Материал 1)
Rectangle(1) = {0, 0, 0, 1, 1, 0};

// Второй прямоугольник (Материал 2)
Rectangle(2) = {1, 0, 0, 1, 1, 0};

// Физические поверхности
Physical Surface("Air") = {1};
Physical Surface("Metal") = {2};

// Общая граница между ними
Physical Curve("Interface") = {2};

// Генерация сетки
Mesh.CharacteristicLengthMin = 0.1;
Mesh.CharacteristicLengthMax = 0.1;
Mesh 2;
"""
    show_code(geo_code_2d, "python")

elif choice == "Пример 3-D":
    st.markdown("##### Пример 3-D")

    geo_code_3d = """
SetFactory("OpenCASCADE");

// Создаем сферу
Sphere(1) = {0, 0, 0, 5};

// Создаем куб
Box(2) = {-3, -3, -3, 6, 6, 6};

// Вычитаем куб из сферы
BooleanDifference(3) = {Volume{1}; Delete;} {Volume{2}; Delete;};

// Физические группы
Physical Volume("Result") = {3};
Physical Surface("CutBoundary") = {2};

// Генерация 3D-сетки
Mesh.CharacteristicLengthMin = 1.0;
Mesh.CharacteristicLengthMax = 1.0;
Mesh 3;
"""
    show_code(geo_code_3d, "python")