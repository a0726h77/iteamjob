## [TortoiseSVN - 下載 SVN for Windows](http://tortoisesvn.net/downloads.html) ##

<br>

<a href='http://blog.ericsk.org/archives/446'>用 Subversion 跟 Google Code 作版本控制 （一）</a>


<a href='http://cire.pixnet.net/blog/post/18373203'>版本控制工具TortoiseSVN初體驗</a>


<a href='http://www.dev.idv.tw/mediawiki/index.php/TortoiseSVN%E4%BD%BF%E7%94%A8%E7%B0%A1%E4%BB%8B'>TortoiseSVN使用簡介</a>


<a href='http://blog.longwin.com.tw/2007/07/svn_tutorial_2007/'>SVN 基本指令教學</a>

<br>

將專案拉回來<br>
<pre><code>$ svn checkout https://iteamjob.googlecode.com/svn/trunk/ iteamjob --username your_account@gmail.com<br>
</code></pre>

在每次修改、提交前, 最好確定主檔案庫伺服器有沒有更新<br>
<pre><code>$ svn update (up)<br>
</code></pre>


將修改後的檔案提交回伺服器<br>
提交時用的是你的google account, 密碼請<a href='https://code.google.com/hosting/settings'>產生你的一次性密碼</a>
<pre><code>$ svn status (st)<br>
$ svn add XXXX<br>
$ svn commit (ci)<br>
</code></pre>

察看提交日誌<br>
<pre><code>$ svn log<br>
<br>
回到以前的修定版 (注意:未commit的檔案修改將會消失)<br>
$ svn update -r 238<br>
</code></pre>

<br>

<h2>在此可<a href='https://code.google.com/p/iteamjob/source/browse/trunk'>瀏覽提交的檔案</a>, 與<a href='https://code.google.com/p/iteamjob/source/list'>察看版本修定資訊</a></h2>