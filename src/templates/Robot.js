import React, { useState } from "react";
import { StyleSheet, Text, View } from "react-native";
import { Button, Image } from "react-native-web";

const Robot = ({navigation, direction}) => {
    return (
    <View style={styles.container}>
       <Image
        source={{uri:"http://localhost:5000/left" }} 
        style = {{ width: 0, height: 0 }}
       />
       <Text>Conveyor has moved {{direction}}</Text>
       <View>
       <Button title='Go back' onPress={() => navigation.navigate('Home')}/>
        </View>
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