# Android发布与构建状态

## 已发布 APK

[v0.20 Android预览版](https://github.com/870255475-del/sen-to-man-ken/releases/tag/v0.20.0-android-preview.1) 已在GitHub公开。下载`SenToManKen_v0.20_Android.apk`，安装后可运行，无需额外SDK/Python。这是免费非商业、仅限18岁以上的制作中预览版。

| 项目 | 实际值 |
| --- | --- |
| Release tag | `v0.20.0-android-preview.1` |
| APK文件 | `SenToManKen_v0.20_Android.apk` |
| 字节数 | `560263182`（约534.3MiB） |
| SHA256 | `43b49acc3c280ac61fab744e11c7a3c44e83c629b139379731dabd6bf05c153d` |
| 包名 / 版本 | `com.sentomanken.game` / `0.20.0` |
| minSdk / targetSdk | `21` / `36` |
| ABI | ARM32 / ARM64 / x86_64 |
| 图形要求 | OpenGL ES3 |
| 横屏 | `sensorLandscape` |
| 工具 | 官方Ren’Py8.5.3 / RAPT |

签名验证通过，并与此前v0.19使用同一签名身份；这不代替设备上的更新安装或存档迁移实测。密钥由维护者私下保管，不提交仓库。

## main与APK的实际差异

main目前是v0.20桌面/内容工作源码公开快照，不包含运行资源，也不是已发布APK的完整可复现构建源。APK另有以下窄改动，**尚未把这些APK专用补丁上传到main**：

1. 为`story_director`及相关剧情资源加载接入Ren’Py归档reader，避免普通系统`open`读取打包路径；实际APK资源通过`renpy.file`/`renpy.open_file`处理。
2. `config.savedir`仅在非Android平台保留桌面自包含`basedir/userdata`行为；Android保留平台默认私有存档位置。
3. 排除34张旧OP帧、旧音轨/视频和12张原字节角色参考，合计48媒体；11角色资料和画廊重映射到既有生成立绘，Q版改用生成宠物。实际205媒体清单和署名随APK提供，不能拿main历史253素材清单直接构建同一发行包。
4. 菜单/旧剧情入口音乐替换为已有许可曲目《和风吹拂》；旧OP播放器改为已有原生图片标题动效。加入菜单预览返回修复，使片头跳过/结束正确回到菜单；增加可滚动“素材署名”页面和Android许可告知。
5. 保留本次16:9中央游戏与整套UI适配，以及超宽侧边/较窄平板上下的场景模糊填充。新APK包含该适配，不再是没有新UI的旧v0.19包。

这些改动属于游戏项目和Android打包适配；本次没有修改Ren’Py引擎。main中仍能看到旧素材路径和桌面存档写法，不应只换SDK/点击RAPT就声称复现了这个APK。等补丁公开后才能按完整对应源重新构建，或自行实施同等窄改动并补齐有发行权限的资源。

## 验证与设备边界

已完成官方RAPT构建，APK签名、全部ZIP成员CRC/SHA、205项媒体逐文件原字节、48项排除及关键源码编译成员核对通过。所选四项SDK touch模拟共124项断言通过，覆盖宽屏1200×540、标准960×540、平板1024×768，以及公开触摸存读档、片头/署名相关入口。

尚未连接Android真机；安装启动、更新兼容、存档迁移、中文输入法、刘海/系统导航安全区、音视频表现和FPS仍需设备验证。SDKtouch模拟不是运行真实APK，也不代表所有剧情路线通关。制作与验证没有真实模型请求。

引擎/组件许可与源码见 [Ren’Py许可入口](https://www.renpy.org/l/license/) 和 [官方源码](https://github.com/renpy/renpy)。素材来源与许可范围见 [ASSET_RIGHTS.md](ASSET_RIGHTS.md) 及APK内“素材署名”页。

用户新提供的泳装动画、带眨眼/呼吸的CG和独立泳池故事属于后续v0.21制作任务，不在本次v0.20 APK中。它们的候选剧情或生图进度不改变这个已发布APK的内容、SHA或验证结论。
