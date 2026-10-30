    # 廣播「某人正在輸入」的狀態給其他人（不含自己）
    emit("typing", data, broadcast=True, include_self=False)