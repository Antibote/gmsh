
    SetFactory("OpenCASCADE");

    // Создаем два куба
    Box(1) = {0, 0, 0, 1, 1, 1};
    Box(2) = {1, 0, 0, 1, 1, 1};

    // Объединяем их через BooleanUnion
    BooleanUnion(3) = {Volume{1}; Delete;} {Volume{2}; Delete;};

    // Назначаем физическую группу на результат
    Physical Volume("Merged_Volumes") = {3};

    // Объединяем границы для сетки
    Compound Surface(200) = {1, 2, 5, 6}; // Внешние грани
    Physical Surface("External_Walls") = {Surface{:}};
                
    Mesh.CharacteristicLengthMin = 0.2;
    Mesh 3;
    