<?php


class add_service {
  public function __construct(){
    print('add_service');

    return;
  }

  public function add_service() {

    $service_name = $_POST['service_name'];
    $service_type = $_POST['service_type'];
    $sevice_address = $_POST['service_address'];

    $SQL = "INSERT INTO `services` VALUES('" . $service_name . "','" . $service_type . "','" . $service_address . "')";
  }
}



?>
