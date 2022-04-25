import React from "react";
import { StyleSheet, Text, View } from "react-native";
import { Button, Image } from "react-native";
import Boxes from "./Boxes";
import Header from "./Header";

const Robot = ({route, navigation}) => {
    const direction = route.params.direction;
    const final = "";
    const url = "http://localhost:5000/"+direction;
    console.log(direction)

    return (
    <View style={styles.container}>
    <Image
        source={{uri:url }} 
        style = {{ width: 0, height: 0 }}
       />
      <Header />
      <Boxes navigation={navigation}/>
      </View>
     );
    };
    
export default Robot;

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center'
    }
  })
