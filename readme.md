# パッケージ生成コマンド一覧

将来的には手順を明確にする。

```
$ conan new lmdb/0.9.22 -t
$ conan source .
$ conan install .
$ conan build . 
$ conan create . toge/stable -keep-build
$ conan info .
```
# パッケージの公開

まだやり方不明。
一度conan-serverをローカルで立てて動作確認が必要みたいだ。


# パッケージの利用方法

以下の通り指定すれば使える、、、らしい。（ただしローカルのみ）

> lmdb/0.9.22@toge/stable

# TODO

- Windowsでのビルド方法を確立
- Sharedでのビルド方法を確立
- pthreadのリンクを賢くやる
