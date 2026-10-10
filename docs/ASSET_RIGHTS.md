# 素材许可与发行范围

本仓库main除一张项目主页宣传PNG外，未跟踪运行美术、音视频、字体或APK。main的素材manifest只记录历史资源路径与SHA，不授予许可。宣传图的来源、改动及共享条件见 [POSTER_CREDITS.md](POSTER_CREDITS.md)，不能由一张宣传图推断其他素材全部获得授权。

另行发布的 [v0.20 Android预览版](https://github.com/870255475-del/sen-to-man-ken/releases/tag/v0.20.0-android-preview.1) 为免费非商业同人制作版。该APK已独立清理、核对并保留来源告知；这不等于把旧APK19或main快照内所有历史素材一并开放发行。

## Android实际媒体范围

已发布APK包含205项媒体，全部与此次清理构建的逐文件SHA/字节数核对一致。相对原v0.20工作素材排除48项：旧OP34帧、旧`festival.ogg`、旧`opening.webm`以及12张原字节角色参考图。205是图片、音频和字体等媒体合计，不能当成CG数量。

角色资料和画廊改用项目已生成的11张中立立绘及Q版捧饭宠物。12张参考图因逐图原作者对应不足而不直接再分发，旧源保留；该排除不是宣称已认定这12图侵权。旧OP/音轨则有具体来源证据：02制作标识与《千恋万花》原片截图SHA一致，旧OP编辑仍保留原作构图/背景/图形；旧音轨与片头视频没有找到可覆盖转载的许可依据。它们确实不在新APK，不能因免费发布而恢复打包。

APK内的`notices/PUBLIC_MEDIA_MANIFEST.json`记录实际205项路径、SHA及来源范围；`notices/PUBLIC_ASSET_CREDITS.txt`可由游戏内“素材署名”页阅读。Android构建与main历史清单的差异另见 [ANDROID_BUILD.md](ANDROID_BUILD.md)。

## 角色设计与项目插图贡献

DeepSeek鲸鱼娘原形象设计来源为 [上善无形 / 上善](https://space.bilibili.com/4456176)，DeepSeek元素及女仆版本二次设计来源为 [ZipZipPipe](https://space.bilibili.com/4168597)。既存声明入口为 [大AI和小AI们](https://www.bilibili.com/video/BV1tE9XBbErS/)，作品入口为 [Pixiv作品148186519](https://www.pixiv.net/artworks/148186519)，项目保留记录载明 [CC BY-NC-SA4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)。

本发行将本项目能够许可的新场景、服装/动作/表情、Q版、衍生图标与界面整合等插图贡献按CC BY-NC-SA4.0分享，保留来源、改动说明、署名、非商业和相同方式共享条件。上游角色设计、原画及其他第三方权利保留；重新生成不自动消除这些权利。该许可不是代码、正文、音乐、字体、引擎或商标的统一许可。

现存记录没有把11角色全部原设计/每张原始参考图逐一映射到同一作者，也没有在本次发行重新独立读取全部作者原页。因此不宣称11个原设计全部由本项目或ZipZipPipe原创，不宣称所有上游权限已逐张核清，不能将本次非商业分享推广成商业授权。同时，旧OP的具体问题也不能扩大成“所有新图都不能非商业分享”。

## 音乐、字体与引擎

六首黑耀耀素材库曲目（《梅》另署名tohka）及四首Kevin MacLeod曲目按逐曲CC BY4.0使用，MP3保持作者原字节，仅运行时循环、音量和淡入淡出。完整作者/曲名/来源/SHA及法律文本在APK的`audio/licensed/`中。Source Han字体保留Adobe/SIL OFL1.1全文，在`fonts/`中。音乐及字体不被图像NC-SA代替许可。

本次未修改Ren’Py引擎。Android告知保留 [Ren’Py组件许可及源码入口](https://www.renpy.org/l/license/) 与 [官方引擎源码](https://github.com/renpy/renpy)，引擎和组件按各自许可使用。

本项目与AI品牌、设计作者和原游戏公司无官方隶属/合作或背书关系。代码公开不等于自动声明开源协议；main尚未选择统一代码许可证，不能用MIT等覆盖人物、第三方音乐、字体与引擎。以后商用、付费推广、品牌联名或单独资产再发行仍需按具体来源核相应权限。
