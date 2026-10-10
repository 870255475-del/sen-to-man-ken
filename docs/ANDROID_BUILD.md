# Android 构建状态

项目使用官方Ren’Py8.5.3 / RAPT，横屏sensorLandscape。既有私有v0.19 APK为签名通用包，minSdk21、targetSdk36、ARM32/ARM64/x86_64、需要OpenGL ES3。该旧APK没有本源码的新16:9侧边适配，且暂不公开分发。

本目录是桌面/内容工作源码，不应直接冒称完整Android构建源。APK资源必须用 `renpy.file` 读取，不能以普通系统open读取打包路径；`story_director.configure_builtin` 需要对应的reader实现。Android上不得把config.savedir设置到安装包basedir/userdata，须保留平台默认私有保存位置；桌面F盘自包含存档行为另保留。

这些适配已在此前独立Android源验证，合并到当前Android工作源并做必要本地检查后，再执行官方RAPT。签名密钥由维护者私下保管，绝不提交。当前源码没有签名密钥、构建缓存或APK。

设备实测仍需检查启动、触摸、存读档、输入法、刘海/导航安全区及音视频表现。SDKtouch模拟并不是运行APK或测量真机FPS。
