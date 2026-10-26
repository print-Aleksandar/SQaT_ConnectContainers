package com.contractplatform;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;
import java.nio.file.Files;

@SpringBootApplication
public class ContractPlatformApplication {

    public static void main(String[] args) {

        // ENV _
        File envFile = new File("../.env");
        if (envFile.exists()) {
            try {
                Files.readAllLines(envFile.toPath()).forEach(line -> {
                    if (line.contains("=") && !line.startsWith("#")) {
                        String[] parts = line.split("=", 2);
                        System.setProperty(parts[0].trim(), parts[1].trim());
                    }
                });
            } catch (Exception ignored) {}
        }
        // ENV ^

        SpringApplication.run(ContractPlatformApplication.class, args);
    }

}