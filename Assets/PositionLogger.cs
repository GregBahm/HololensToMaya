using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PositionLogger : MonoBehaviour
{
	void Start ()
    {
        Debug.Log("Begin Position Logger");
	}
	
	void Update ()
    {
        string stringSuffix = "Logger for Andy";
        string timePart = Time.frameCount.ToString();
        string positionPart = transform.position.x + " " + transform.position.y + " " + transform.position.z;
        string rotationPart = transform.rotation.eulerAngles.x + " " + transform.rotation.eulerAngles.y + " " + transform.rotation.eulerAngles.z;
        string finalString = string.Format("{0},{1},{2},{3}", stringSuffix, timePart, positionPart, rotationPart);
        Debug.Log(finalString);
    }
}