/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.allthefeels;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.core.MediaType;
import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import javax.ws.rs.PathParam;

/**
 * REST Web Service
 *
 * @author josepena
 */
@Path("allthefeels")
public class AllTheFeels {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of AllTheFeels
     */
    public AllTheFeels() {
    }

    /**
     * Retrieves representation of an instance of com.allthefeels.AllTheFeels
     * @return an instance of java.lang.String
     */
    @GET
    @Path("spotify/{url}")
    public void deploySpotify(@PathParam("url") String url) throws URISyntaxException, IOException {
        if(Desktop.isDesktopSupported())
        {

            System.out.println(url.replaceAll(":", "/"));
            Desktop.getDesktop().browse(new URI("https://open.spotify.com"+url.replaceAll(":", "/").substring(7)));
	}
    }

    /**
     * PUT method for updating or creating an instance of AllTheFeels
     * @param content representation for the resource
     */
    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public void putJson(String content) {
    }
}
