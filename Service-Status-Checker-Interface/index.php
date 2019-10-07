<?php
# Author: Traivs-Owens
# Date: 2019-8-17
# Description: Interface for managing the service-status-checker database entries.


if(isset($_GET['page'])) {

  if($_GET['page'] == 'manage_services') {
    require_once('views/manage_services.php');
    $manage_obj = New manage_services();
  }

  if($_GET['page'] == 'add_service') {
    require_once('views/add_service.php');
    $add_obj = New add_service();
  }

  if($_GET['page'] == 'test') {
    print('test');
  }
} else {

  # Manage Services
  echo("<a href='index.php?page=manage_services'> Manage Services </a> <br>");
  echo("<a href='index.php?page=add_service'> Add Services </a>");


}





// $routes = array(
//   "mange_services" => array(
//       "page" => 'manage_services',
//       "route" => 'views/manage_services.php',
//       "template" => 'login_page',
//     ),
// );
//
// // print_r($routes);
//
//
//
//   foreach ($routes as $i) {
//       print_r($i)
//     }
?>
