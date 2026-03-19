import streamlit as st
from PIL import Image
import base64
import subprocess
import os
import math
import gmsh
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import plotly.graph_objects as go  # Для 3D-визуализации
st.set_page_config(page_title="🗓", layout="wide")

# Функция для отображения кода с возможностью копирования
def show_code(code, language="python"):
    st.code(code, language)

def run_gmsh(file_path):
    try:
        env = os.environ.copy()
        env["LIBGL_ALWAYS_SOFTWARE"] = "1"  # Используем программный рендеринг
        subprocess.run(["gmsh", file_path], check=True, env=env)
        st.success("Gmsh успешно запущен в программном режиме!")
    except FileNotFoundError:
        st.error("Gmsh не найден. Убедитесь, что он установлен и доступен в PATH.")
    except subprocess.CalledProcessError as e:
        st.error(f"Ошибка при запуске Gmsh: {e.returncode}")
        st.text(f"Вывод ошибки:\n{e.stderr}")

sections = {
    "Поддерживаемые сеточные форматы": "",
    "Пример подготовки сетки с граничными условиями": "",
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))
    
if choice == "Поддерживаемые сеточные форматы":
    st.markdown("##### Поддерживаемые сеточные форматы")

    with st.expander("1. Собственный формат FEniCS (XML)"):
        st.write("""
        - FEniCS изначально использует XML-формат для хранения сеток и данных.
        - Примеры файлов:
            - `mesh.xml` — файл сетки.
            - `mesh_facet_region.xml` — файл с метками граничных элементов.
            - `mesh_physical_region.xml` — файл с метками физических областей.
        - Эти файлы создаются с помощью утилиты `dolfin-convert` или вручную.
        """)

    with st.expander("2. Форматы, поддерживаемые через dolfin-convert"):
        st.write("""
        Утилита dolfin-convert позволяет конвертировать сетки из других форматов в формат, понятный FEniCS.
        - Поддерживаемые форматы:
            - **Gmsh (.msh)**
            - **MEDIT (.mesh)**
            - **Triangle (.node, .ele)**
            - **TetGen (.node, .ele)**
        """)
        st.code("dolfin-convert input_mesh.msh output_mesh.xml", language="bash")


    with st.expander("3. Формат XDMF"):
        st.write("""
        - XDMF (eXtensible Data Model and Format) поддерживает хранение сеток и данных.
        - Используется для больших сеток и параллельных вычислений.
        """)
        st.code("""
        from dolfin import *
        mesh = Mesh()
        with XDMFFile("mesh.xdmf") as infile:
            infile.read(mesh)
        with XDMFFile("output_mesh.xdmf") as outfile:
            outfile.write(mesh)
        """, language="python")

    with st.expander("4. Формат VTK"):
        st.write("""
        - VTK (Visualization Toolkit) используется для визуализации данных.
        - FEniCS может экспортировать результаты в VTK для визуализации в ParaView.
        """)
        st.code("""
        from dolfin import *
        mesh = UnitSquareMesh(10, 10)
        V = FunctionSpace(mesh, 'P', 1)
        u = Function(V)
        File("output.pvd") << u
        """, language="python")

    with st.expander("5. Другие форматы"):
        st.write("""
        - **HDF5**: используется для хранения больших данных и сеток.
        - **DOLFIN HDF5**: специальный формат для хранения сеток и данных в FEniCS.
        - **NETCDF**: поддерживается для работы с данными.
        """)

    with st.expander("Некоторые рекомендации"):
        st.write("""
        - Для простых задач использовать XML-формат.
        - Для больших сеток и параллельных вычислений лучше подходят XDMF или HDF5.
        - Для подготовки сетки в FEniCS нужно использовать Gmsh, mshr или другие инструменты. 
        - Конвертировать сетку в формат `.xml` или `.xdmf` с помощью `meshio` или `dolfin-convert`.
        """)

elif choice == "Пример подготовки сетки с граничными условиями":
    st.markdown("##### Пример подготовки сетки с граничными условиями")
    st.write("""
    ```bash
    import meshio

    # Чтение .msh файла
    mesh = meshio.read("mesh_with_bc.msh")
    # Запись в .xdmf формат
    meshio.write("mesh_with_bc.xdmf", mesh)
    from fenics import *

    # Загрузка сетки
    mesh = Mesh()
    with XDMFFile("mesh_with_bc.xdmf") as infile:
        infile.read(mesh)

    # Загрузка граничных меток
    boundaries = MeshFunction("size_t", mesh, mesh.topology().dim() - 1)
    with XDMFFile("mesh_with_bc_boundaries.xdmf") as infile:
        infile.read(boundaries)

    # Определение граничных условий
    u_D = Constant(0.0)
    bc = DirichletBC(V, u_D, boundaries, 1)  # 1 — идентификатор границы

    # Визуализация граничных меток
    plot(boundaries)
    plt.title("Boundary Markers")
    plt.show()
              """)
