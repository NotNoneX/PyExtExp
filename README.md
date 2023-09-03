# Python 浏览器扩展导出

这是一个用于生成浏览器扩展（Chrome 扩展）的 Python
工具。它允许你从指定目录中查找浏览器扩展目录，并生成相关信息，例如浏览器扩展名、版本等。此工具还支持配置文件，以便为每个生成的扩展指定特定参数。

## 功能

1. 查找指定目录中的浏览器扩展目录。
2. 解析扩展目录下的信息，包括名称、版本等。
3. 支持配置文件以指定浏览器类型、目录和输出路径。
4. 生成浏览器扩展文件（.crx）并附带私钥。

## 代码结构

- `main.py` - 包含主要的执行逻辑，配置文件读取和生成扩展功能。
- `common/create_crx.py` - 实现了生成浏览器扩展文件的功能。

## 用法

1. 首先，配置 `config.ini` 文件，指定浏览器类型、扩展目录、私钥路径和生成文件路径。
2. 使用 `main.py` 执行主程序，它将查找扩展目录并生成浏览器扩展文件。

> 注意 运行文件前, 请确保已正确配置好文件config.ini

### 配置文件说明

示例配置文件: config.example.ini
请修改config.ini配置文件用于本项目配置

```ini
; type: 指定浏览器类型, 如: chrome(暂只支持Chrome浏览器)
[Browser]
type = Chrome

; extensions_dir: 配置浏览器扩展路径, 路径取至: Your\Browser\Path\...\Extensions
; 例如: 谷歌浏览器默认扩展路径: C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data\Default\Extensions
; Pem_Path: 私钥文件保存路径
; Crx_Path: 扩展文件保存路径
[Options]
extensions_dir = 你的浏览器扩展路径
pem_path = 私钥文件保存路径
crx_path = 扩展文件导出路径
```

### 示例用法：

```bash
python main.py
```

