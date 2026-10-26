package com.contractplatform.service;

import com.contractplatform.domain.models.Client;
import com.contractplatform.domain.models.ClientUserDetails;
import com.contractplatform.repository.ClientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;


@RequiredArgsConstructor
public class ClientService implements IClientService{

    private final ClientRepository clientRepository;
    private final UserDetailsService userDetailsService;

    @Override
    public void registerClient(Client client) {

        try {
            ClientUserDetails foundDetails = (ClientUserDetails) userDetailsService.loadUserByUsername(client.getEmail());
            Client foundClient = foundDetails.getClient();

            throw new RuntimeException("Email is already registered");

        } catch (UsernameNotFoundException untEx) {
            clientRepository.save(client)
        }

    }
}
