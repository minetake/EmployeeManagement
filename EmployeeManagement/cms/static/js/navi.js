function sidemenu(id,sid) {
	
	var activeObj = new Object();
	var activeSubObj = new Object();
	
	activeObj['index']        = '';
	activeObj['graph']        = '';
	activeObj['skill_edit']   = ' class="treeview" ';
	activeObj['project_edit'] = '';
	activeObj['skill']        = '';
	activeObj['search']       = ' class="treeview" ';
	
	activeSubObj['engineer']  = '';
	activeSubObj['maps']      = '';
	activeSubObj['program']   = '';
	activeSubObj['environment']  = '';
	
	activeObj[id] = ' class="active" ';
	if ( sid ) {
		activeSubObj[sid] = ' class="active" ';
	}
	
	var html = "";
	
//    html += '<nav class="navbar navbar-static-top">';
//    html += '        <div class="navbar-custom-menu">';
//    html += '            <ul class="nav navbar-nav">';
    html += '                <li' + activeObj['index'] + '>';
    html += '                    <a href="/index/"><i class="fa fa-diamond"></i> <span class="nav-label">DashBoard</span></a>';
    html += '                </li>';                                      
    html += '                <li' + activeObj['search'] + '>';
    html += '                    <a href="#"><i class="fa fa-table"></i> <span class="nav-label">技術者検索</span><span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span></a>';
    html += '                    <ul class="treeview-menu">';
    html += '                        <li' + activeSubObj['engineer'] + '><a href="/engineer/">技術者一覧</a></li>';
    html += '                        <li' + activeSubObj['maps'] + '><a href="/maps/">就業場所</a></li>';
    html += '                    </ul>';
    html += '                </li>';
//    html += '                <li' + activeObj['graph'] + '>';
//    html += '                    <a href="graph.html"><i class="fa fa-bar-chart-o"></i> <span class="nav-label">グラフ</span></a>';
//    html += '                </li>';
//    html += '                <li' + activeObj['skill_edit'] +'>';
//    html += '                    <a href="/skill-edit/"><i class="fa fa-edit"></i> <span class="nav-label">スキル編集</span></a>';
//    html += '                </li>';
    html += '                <li' + activeObj['skill_edit'] + '>';
    html += '                    <a href="#"><i class="fa fa-table"></i> <span class="nav-label">スキル編集</span><span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span></a>';
    html += '                    <ul class="treeview-menu">';
    html += '                        <li' + activeSubObj['program'] + '><a href="/skill-edit/list/program/">プログラム</a></li>';
    html += '                        <li' + activeSubObj['environment'] + '><a href="/skill-edit/list/enviroment/">環境</a></li>';
    html += '                    </ul>';
    html += '                </li>';    
    html += '                <li' + activeObj['project_edit'] + '>';
    html += '                    <a href="/project-edit/"><i class="fa fa-database"></i> <span class="nav-label">プロジェクト新規登録</span></a>';
    html += '                </li>';
    html += '                <li' + activeObj['skill'] + '>';
    html += '                    <a href="/skill/"><i class="fa fa-files-o"></i> <span class="nav-label">スキルシート編集・印刷</span></a>';
    html += '                </li>';
//    html += '            </ul>';
//    html += '        </div>';
//    html += '    </nav>';

	document.write(html);
  
}  

function topbar() {
	
	html += '	 <nav class="navbar navbar-static-top" style="margin-bottom: 0">';
    html += '    <div class="navbar-header">';
    html += '        <a class="navbar-minimalize minimalize-styl-2 btn btn-primary" href="#"><i class="fa fa-bars"></i></a>';
    html += '        <form role="search" class="navbar-form-custom" action="search_results.html">';
    html += '            <div class="form-group">';
    html += '                <input type="text" placeholder="Search for something..." class="form-control" name="top-search" id="top-search">';
    html += '            </div>';
    html += '        </form>';
    html += '    </div>';
    html += '        <ul class="nav navbar-top-links navbar-right">';
    html += '            <li>';
    html += '                <span class="m-r-sm text-muted welcome-message">Welcome to INSPINIA+ Admin Theme.</span>';
    html += '            </li>';
    html += '            <li class="dropdown">';
    html += '                <a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">';
    html += '                    <i class="fa fa-envelope"></i>  <span class="label label-warning">16</span>';
    html += '                </a>';
    html += '                <ul class="dropdown-menu dropdown-messages">';
    html += '                    <li>';
    html += '                        <div class="dropdown-messages-box">';
    html += '                            <a href="profile.html" class="pull-left">';
    html += '                                <img alt="image" class="img-circle" src="img/a7.jpg">';
    html += '                            </a>';
    html += '                            <div class="media-body">';
    html += '                                <small class="pull-right">46h ago</small>';
    html += '                                <strong>Mike Loreipsum</strong> started following <strong>Monica Smith</strong>. <br>';
    html += '                                <small class="text-muted">3 days ago at 7:58 pm - 10.06.2014</small>';
    html += '                            </div>';
    html += '                        </div>';
    html += '                    </li>';
    html += '                    <li class="divider"></li>';
    html += '                    <li>';
    html += '                        <div class="dropdown-messages-box">';
    html += '                            <a href="profile.html" class="pull-left">';
    html += '                                <img alt="image" class="img-circle" src="img/a4.jpg">';
    html += '                            </a>';
    html += '                            <div class="media-body ">';
    html += '                                <small class="pull-right text-navy">5h ago</small>';
    html += '                                <strong>Chris Johnatan Overtunk</strong> started following <strong>Monica Smith</strong>. <br>';
    html += '                                <small class="text-muted">Yesterday 1:21 pm - 11.06.2014</small>';
    html += '                            </div>';
    html += '                        </div>';
    html += '                    </li>';
    html += '                    <li class="divider"></li>';
    html += '                    <li>';
    html += '                        <div class="dropdown-messages-box">';
    html += '                            <a href="profile.html" class="pull-left">';
    html += '                                <img alt="image" class="img-circle" src="img/profile.jpg">';
    html += '                            </a>';
    html += '                            <div class="media-body ">';
    html += '                                <small class="pull-right">23h ago</small>';
    html += '                                <strong>Monica Smith</strong> love <strong>Kim Smith</strong>. <br>';
    html += '                                <small class="text-muted">2 days ago at 2:30 am - 11.06.2014</small>';
    html += '                            </div>';
    html += '                        </div>';
    html += '                    </li>';
    html += '                    <li class="divider"></li>';
    html += '                    <li>';
    html += '                        <div class="text-center link-block">';
    html += '                            <a href="mailbox.html">';
    html += '                                <i class="fa fa-envelope"></i> <strong>Read All Messages</strong>';
    html += '                            </a>';
    html += '                        </div>';
    html += '                    </li>';
    html += '                </ul>';
    html += '            </li>';
    html += '            <li class="dropdown">';
    html += '                <a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">';
    html += '                    <i class="fa fa-bell"></i>  <span class="label label-primary">8</span>';
    html += '                </a>';
    html += '                <ul class="dropdown-menu dropdown-alerts">';
    html += '                    <li>';
    html += '                        <a href="mailbox.html">';
    html += '                            <div>';
    html += '                                <i class="fa fa-envelope fa-fw"></i> You have 16 messages';
    html += '                                <span class="pull-right text-muted small">4 minutes ago</span>';
    html += '                            </div>';
    html += '                        </a>';
    html += '                    </li>';
    html += '                    <li class="divider"></li>';
    html += '                    <li>';
    html += '                        <a href="profile.html">';
    html += '                            <div>';
    html += '                                <i class="fa fa-twitter fa-fw"></i> 3 New Followers';
    html += '                                <span class="pull-right text-muted small">12 minutes ago</span>';
    html += '                            </div>';
    html += '                        </a>';
    html += '                    </li>';
    html += '                    <li class="divider"></li>';
    html += '                    <li>';
    html += '                        <a href="grid_options.html">';
    html += '                            <div>';
    html += '                                <i class="fa fa-upload fa-fw"></i> Server Rebooted';
    html += '                                <span class="pull-right text-muted small">4 minutes ago</span>';
    html += '                            </div>';
    html += '                        </a>';
    html += '                    </li>';
    html += '                    <li class="divider"></li>';
    html += '                    <li>';
    html += '                        <div class="text-center link-block">';
    html += '                            <a href="notifications.html">';
    html += '                                <strong>See All Alerts</strong>';
    html += '                                <i class="fa fa-angle-right"></i>';
    html += '                            </a>';
    html += '                        </div>';
    html += '                    </li>';
    html += '                </ul>';
    html += '            </li>';


    html += '            <li>';
    html += '                <a href="login.html">';
    html += '                    <i class="fa fa-sign-out"></i> Log out';
    html += '                </a>';
    html += '            </li>';
    html += '            <li>';
    html += '                <a class="right-sidebar-toggle">';
    html += '                    <i class="fa fa-tasks"></i>';
    html += '                </a>';
    html += '            </li>';
    html += '        </ul>';

    html += '    </nav>';

	document.write(html);	
		
}

